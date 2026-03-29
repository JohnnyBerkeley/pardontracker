"""
Trump Money Map — Update Search Script
Run this to find new incidents since the last update date.
Requires: pip install requests duckduckgo-search

Usage:
    python scripts/update_search.py
    python scripts/update_search.py --since 2026-02-01
"""

import json
import sys
import argparse
from datetime import date, datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_last_updated() -> str:
    incidents_path = DATA_DIR / "incidents.json"
    with open(incidents_path) as f:
        data = json.load(f)
    return data.get("last_updated", "2025-01-20")


SEARCH_QUERIES = {
    "crypto_sales": [
        "Trump memecoin TRUMP crypto corruption conflict interest",
        "World Liberty Financial WLFI foreign investment",
        "Trump crypto stablecoin USD1 deal",
    ],
    "selling_access": [
        "Trump Mar-a-Lago foreign officials emoluments",
        "Trump selling access president dinner event",
    ],
    "foreign_gift": [
        "Trump foreign gift donation airplane plane",
        "Trump emoluments foreign government payment",
    ],
    "insider_trading": [
        "Trump insider trading market manipulation allegations",
        "Trump Truth Social trading stock before announcement",
        "Trump tariff trading suspicion investigation",
        "Trump Iran oil futures trading insider",
    ],
    "power_abuse": [
        "Trump regulatory coercion law firm settlement 2025",
        "Trump university settlement coercion",
        "Trump holding back deal approval leverage",
        "Trump DOGE political targeting company",
    ],
    "family_enrichment": [
        "Jared Kushner Affinity Partners Middle East investment",
        "Trump family business foreign money deal",
        "Eric Trump Don Jr business deal foreign",
    ],
    "state_damages": [
        "Trump lawsuit government IRS Treasury damages",
        "Trump allies seeking damages government forgiven",
    ],
    "pardons": [
        "Trump pardon commutation financial connection donor",
        "Trump pardon restitution forgiven",
        "Trump new pardons",
    ],
    "arms_deal_conflict": [
        "Trump arms deal Saudi UAE conflict interest business",
    ],
}

# Top watchdog and investigative sources to monitor manually
MONITOR_SOURCES = [
    {
        "name": "CREW — Trump conflicts tracker",
        "url": "https://www.citizensforethics.org/reports-investigations/",
        "description": "Citizens for Responsibility and Ethics in Washington"
    },
    {
        "name": "ProPublica — Trump investigations",
        "url": "https://www.propublica.org/topics/trump",
        "description": "Investigative journalism"
    },
    {
        "name": "OpenSecrets — Trump PAC and donation tracking",
        "url": "https://www.opensecrets.org/",
        "description": "Campaign finance data"
    },
    {
        "name": "DOJ Pardon Attorney — official clemency list",
        "url": "https://www.justice.gov/pardon/clemency-grants-president-donald-j-trump-2025-present",
        "description": "Official pardon records"
    },
    {
        "name": "American Oversight — taxpayer spending at Trump properties",
        "url": "https://americanoversight.org/tracking-taxpayer-spending-at-trump-properties/",
        "description": "FOIA-based spending tracker"
    },
    {
        "name": "Sunlight Foundation — Trump conflicts tracker",
        "url": "https://trumpconflicts.sunlightfoundation.com/",
        "description": "Comprehensive conflicts database"
    },
    {
        "name": "Lawfare — Trump litigation tracker",
        "url": "https://www.lawfaremedia.org/projects-series/trials-of-the-trump-administration/tracking-trump-administration-litigation",
        "description": "Legal proceedings tracking"
    },
]


def print_search_plan(since_date: str):
    print(f"\n{'='*60}")
    print(f"Trump Money Map — Update Search")
    print(f"Searching for incidents SINCE: {since_date}")
    print(f"{'='*60}\n")
    print("SEARCH QUERIES TO RUN (add 'after:{since_date}' to each):\n")
    for category, queries in SEARCH_QUERIES.items():
        print(f"  [{category}]")
        for q in queries:
            print(f"    \"{q} after:{since_date}\"")
        print()
    print("\nSOURCES TO CHECK MANUALLY:")
    for source in MONITOR_SOURCES:
        print(f"  - {source['name']}")
        print(f"    {source['url']}")
    print()


def get_incident_template(since_date: str) -> dict:
    """Returns a blank incident template for manual entry."""
    return {
        "id": "FILL-IN-slug-YYYY-MM",
        "date": "YYYY-MM-DD",
        "date_end": None,
        "title": "FILL IN",
        "summary": "FILL IN",
        "categories": [],
        "status": "confirmed | alleged | suspected | denied",
        "beneficiary": [],
        "actors": [],
        "amount_usd": None,
        "amount_note": "FILL IN",
        "financial_connection": {
            "exists": None,
            "description": "FILL IN"
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": None,
            "received": None
        },
        "sources": [
            {
                "title": "FILL IN",
                "url": "FILL IN",
                "date": "YYYY-MM-DD",
                "outlet": "FILL IN",
                "type": "news | official | watchdog | congressional"
            }
        ],
        "tags": [],
        "last_updated": date.today().isoformat()
    }


def update_last_searched(data_file: Path, new_date: str):
    with open(data_file) as f:
        data = json.load(f)
    data["last_updated"] = new_date
    with open(data_file, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated last_updated in {data_file.name} to {new_date}")


def main():
    parser = argparse.ArgumentParser(description="Generate update search queries for Trump Money Map")
    parser.add_argument(
        "--since",
        type=str,
        help="Search for incidents since this date (YYYY-MM-DD). Defaults to last_updated in incidents.json.",
        default=None
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Print a blank incident JSON template for manual entry"
    )
    args = parser.parse_args()

    since_date = args.since or load_last_updated()

    print_search_plan(since_date)

    if args.template:
        print("\nBLANK INCIDENT TEMPLATE:")
        print(json.dumps(get_incident_template(since_date), indent=2))

    print(f"\nAfter adding new incidents to data/incidents.json,")
    print(f"run: python scripts/update_search.py --mark-updated")
    print(f"to record today ({date.today().isoformat()}) as the new search date.\n")


if __name__ == "__main__":
    main()
