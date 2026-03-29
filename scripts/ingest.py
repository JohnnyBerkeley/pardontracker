"""
Trump Money Map — AI-powered ingestion pipeline
================================================
Processes URLs or pasted article text, calls Claude API to generate
draft incident JSON following the project's editorial rules, then
lets you review before writing to incidents.json.

Usage
-----
  # Process a single URL:
  python scripts/ingest.py --url https://www.nytimes.com/...

  # Process multiple URLs from a file (one per line):
  python scripts/ingest.py --urlfile inbox.txt

  # Process pasted text (reads from stdin):
  python scripts/ingest.py --stdin

  # Auto-approve and write without interactive review:
  python scripts/ingest.py --url https://... --yes

  # Dry run: print drafts but don't write anything:
  python scripts/ingest.py --url https://... --dry

Requirements
------------
  pip install anthropic httpx

Set your API key:
  Windows:  set ANTHROPIC_API_KEY=sk-ant-...
  Or pass:  python scripts/ingest.py --url ... --api-key sk-ant-...
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

try:
    import anthropic
    import httpx
except ImportError:
    print("Missing dependencies. Run: pip install anthropic httpx")
    sys.exit(1)

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE = Path(__file__).parent.parent
INCIDENTS_FILE = BASE / "data" / "incidents.json"
PARDONS_FILE   = BASE / "data" / "pardons.json"
RULES_FILE     = BASE / "EDITORIAL_RULES.md"
SCHEMA_FILE    = BASE / "data" / "schema.md"

# ── System prompt ─────────────────────────────────────────────────────────────
def build_system_prompt() -> str:
    rules  = RULES_FILE.read_text(encoding="utf-8")
    schema = SCHEMA_FILE.read_text(encoding="utf-8")

    with open(INCIDENTS_FILE, encoding="utf-8") as f:
        idata = json.load(f)

    existing_summary = "\n".join(
        f"  - {inc['id']}: {inc['title'][:80]}"
        for inc in idata["incidents"]
    )

    return f"""You are a data journalist working on the "Trump Money Map" project for DN Media Group (a Norwegian financial newspaper). Your job is to process news articles or URLs and extract structured incident data following the project's strict editorial rules.

=== EDITORIAL RULES ===
{rules}

=== DATA SCHEMA ===
{schema}

=== EXISTING INCIDENTS (to avoid duplicates) ===
{existing_summary}

=== YOUR TASK ===
Given a news article or URL content, determine whether it qualifies as a new incident under the editorial rules. If yes, produce a complete JSON incident object. If no, explain why it does not qualify or suggest updating an existing incident.

OUTPUT FORMAT
-------------
Always respond with a JSON object in this exact structure:

{{
  "action": "add" | "update" | "skip",
  "reason": "brief explanation of your decision",
  "incident": {{ ... complete incident JSON if action=add ... }},
  "update_id": "existing-incident-id if action=update",
  "update_notes": "what should change in the existing entry if action=update"
}}

If action is "add", the "incident" field must be a complete, valid incident JSON object following the schema exactly. Generate a slug ID in the format "counterparty-name-YYYY-MM" using lowercase and hyphens.

If action is "skip", explain what threshold the article failed to meet.

If action is "update", name the existing incident ID and describe what new information should be added to it.

TODAY'S DATE: {date.today().isoformat()}
"""

# ── Fetch URL content ─────────────────────────────────────────────────────────
def fetch_url(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        resp = httpx.get(url, headers=headers, timeout=20, follow_redirects=True)
        resp.raise_for_status()
        text = resp.text
        text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.DOTALL)
        text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        words = text.split()
        if len(words) > 6000:
            text = " ".join(words[:6000]) + "\n[... article truncated ...]"
        return text
    except Exception as e:
        return f"[Could not fetch URL: {e}]"


# ── Call Claude API ───────────────────────────────────────────────────────────
def call_claude(system_prompt: str, content: str, api_key: str) -> dict:
    client = anthropic.Anthropic(api_key=api_key)

    user_message = f"""Please analyze this article and produce the structured JSON output as instructed.

ARTICLE CONTENT:
{content}
"""
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )

    raw = message.content[0].text.strip()

    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    if json_match:
        raw = json_match.group(1)
    else:
        start = raw.find("{")
        end   = raw.rfind("}") + 1
        if start != -1 and end > start:
            raw = raw[start:end]

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"\n[WARNING] Could not parse Claude response as JSON: {e}")
        print("Raw response:")
        print(raw[:2000])
        return {"action": "error", "reason": f"JSON parse error: {e}", "raw": raw}


# ── Review and write ──────────────────────────────────────────────────────────
def review_and_write(result: dict, source_url: str, dry: bool, auto_yes: bool) -> bool:
    action = result.get("action", "error")
    reason = result.get("reason", "")

    print(f"\n{'='*60}")
    print(f"ACTION: {action.upper()}")
    print(f"REASON: {reason}")

    if action == "skip":
        print("Not added to dataset.")
        return False

    if action == "update":
        print(f"Suggests updating existing incident: {result.get('update_id')}")
        print(f"  Notes: {result.get('update_notes')}")
        print("Please update manually.")
        return False

    if action in ("error", ""):
        print("Claude returned an error. Check raw output above.")
        return False

    if action != "add":
        print(f"Unknown action '{action}'. Skipping.")
        return False

    incident = result.get("incident")
    if not incident:
        print("No incident data returned.")
        return False

    sources = incident.get("sources", [])
    urls_in_sources = [s.get("url", "") for s in sources]
    if source_url and source_url not in urls_in_sources:
        sources.append({
            "title": "Source article",
            "url": source_url,
            "date": date.today().isoformat(),
            "outlet": "",
            "type": "news"
        })
        incident["sources"] = sources

    if "last_updated" not in incident:
        incident["last_updated"] = date.today().isoformat()
    if "motivation" not in incident:
        incident["motivation"] = "political"

    print("\n--- DRAFT INCIDENT ---")
    draft_str = json.dumps(incident, indent=2, ensure_ascii=False)
    print(draft_str[:3000])
    if len(draft_str) > 3000:
        print("[... truncated for display ...]")

    if dry:
        print("\n[DRY RUN] Not writing to file.")
        return False

    if not auto_yes:
        answer = input("\nAdd this incident to incidents.json? [y/N] ").strip().lower()
        if answer != "y":
            print("Skipped.")
            return False

    with open(INCIDENTS_FILE, encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = [inc["id"] for inc in data["incidents"]]
    if incident.get("id") in existing_ids:
        new_id = incident["id"] + "-v2"
        print(f"[WARNING] ID '{incident['id']}' already exists. Using '{new_id}'.")
        incident["id"] = new_id

    data["incidents"].append(incident)
    data["last_updated"] = date.today().isoformat()

    with open(INCIDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nAdded '{incident['id']}' to incidents.json")
    print(f"Total incidents: {len(data['incidents'])}")
    print(f"\nRun 'python scripts/build_html.py' to rebuild the explorer.")
    return True


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Trump Money Map ingestion pipeline")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--url",     help="Single URL to process")
    src.add_argument("--urlfile", help="File with URLs, one per line")
    src.add_argument("--stdin",   action="store_true", help="Read article text from stdin")
    parser.add_argument("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY)")
    parser.add_argument("--dry",  action="store_true", help="Print drafts, don't write")
    parser.add_argument("--yes",  action="store_true", help="Auto-approve all additions")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: Set ANTHROPIC_API_KEY environment variable or pass --api-key")
        sys.exit(1)

    print("Loading rules, schema, existing incidents...")
    system_prompt = build_system_prompt()
    print(f"System prompt ready ({len(system_prompt)} chars)")

    items = []

    if args.url:
        print(f"\nFetching: {args.url}")
        content = fetch_url(args.url)
        items.append((args.url, content))

    elif args.urlfile:
        urls = Path(args.urlfile).read_text(encoding="utf-8").splitlines()
        urls = [u.strip() for u in urls if u.strip() and not u.startswith("#")]
        print(f"\nFound {len(urls)} URLs in {args.urlfile}")
        for url in urls:
            print(f"Fetching: {url}")
            content = fetch_url(url)
            items.append((url, content))

    elif args.stdin:
        print("Paste article text. Press Ctrl+Z (Windows) or Ctrl+D (Unix) when done:")
        content = sys.stdin.read()
        items.append(("", content))

    added = 0
    for i, (url, content) in enumerate(items):
        print(f"\n[{i+1}/{len(items)}] Processing: {url or '(stdin)'}")
        print(f"  Content: {len(content)} chars")

        result = call_claude(system_prompt, f"SOURCE URL: {url}\n\n{content}", api_key)
        written = review_and_write(result, url, dry=args.dry, auto_yes=args.yes)
        if written:
            added += 1
            system_prompt = build_system_prompt()  # refresh to include new entry

    print(f"\n{'='*60}")
    print(f"Done. Added {added}/{len(items)} incidents.")
    if added > 0 and not args.dry:
        print("Next steps:")
        print("  python scripts/build_html.py")
        print("  git add data/incidents.json index.html && git commit -m 'Add new incidents'")


if __name__ == "__main__":
    main()
