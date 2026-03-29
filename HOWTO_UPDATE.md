# How to Keep the Dataset Current

Two strategies — use either or both.

---

## Strategy A: Drop URLs into this chat (Claude does the work)

Paste one or more URLs directly into the chat with Claude Code.
Claude will fetch the content, apply the editorial rules in
`EDITORIAL_RULES.md`, and add the incident to `incidents.json`.

**Best for:** Occasional updates, stories you spot while reading the news.

---

## Strategy B: Run the automated ingestion script

The script `scripts/ingest.py` sends each article to the Claude API,
applies all the editorial rules automatically, and presents a draft for
your review before writing to the database.

### One-time setup

```bash
pip install anthropic httpx
```

Get an API key from https://console.anthropic.com and set it:

```bash
# Windows (Command Prompt)
set ANTHROPIC_API_KEY=sk-ant-api03-...

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."
```

To make it permanent: add to System Environment Variables in Windows Settings.

### Usage

**Single URL:**
```bash
python scripts/ingest.py --url https://www.nytimes.com/2026/04/01/...
```

**Multiple URLs (batch):**
```bash
# Add URLs to inbox.txt (one per line)
python scripts/ingest.py --urlfile inbox.txt
```

**Paste article text directly:**
```bash
python scripts/ingest.py --stdin
# (paste text, then press Ctrl+Z on Windows to finish)
```

**Dry run (see what would be added, don't write):**
```bash
python scripts/ingest.py --url https://... --dry
```

**Auto-approve all (no interactive review):**
```bash
python scripts/ingest.py --urlfile inbox.txt --yes
```

### After adding incidents

```bash
python scripts/build_html.py
git add data/incidents.json index.html
git commit -m "Add new incidents via ingest script"
git push
```

---

## How the script decides what to add

The script reads three files before calling Claude:

1. **`EDITORIAL_RULES.md`** — The full rules: what qualifies, how to classify,
   status/motivation/category definitions, source standards, thresholds.
2. **`data/schema.md`** — The JSON schema for all fields.
3. **`data/incidents.json`** — Existing incidents (to avoid duplicates).

Claude then produces one of:
- **add** — Draft incident JSON. You review and approve.
- **update** — The story belongs in an existing entry; it names which one.
- **skip** — The story doesn't meet the threshold; it explains why.

---

## Periodic sweep (every 2-4 weeks)

Run `update_search.py` to get date-bounded search queries for each category:

```bash
python scripts/update_search.py
```

Copy the queries into Google or a news search engine, collect relevant URLs,
add them to `inbox.txt`, then run the ingest script.

---

## If something looks wrong

The script always asks for confirmation before writing (unless `--yes` is used).
If a draft looks off, reject it and either:
- Paste the URL into a Claude chat session to handle manually
- Edit `EDITORIAL_RULES.md` to clarify the edge case for future runs

---

## Key files

| File | Purpose |
|---|---|
| `EDITORIAL_RULES.md` | All editorial judgment rules — the project's "constitution" |
| `data/schema.md` | JSON field definitions for all data types |
| `scripts/ingest.py` | Automated ingestion pipeline (calls Claude API) |
| `scripts/build_html.py` | Rebuilds `index.html` from JSON data |
| `scripts/update_search.py` | Generates search queries for periodic sweeps |
| `inbox.txt` | Drop URLs here for batch processing |
| `data/incidents.json` | Main incident database (69 entries as of 2026-03-30) |
| `data/pardons.json` | Pardon database |
| `data/constitutional_violations.json` | Constitutional challenges tracker |
