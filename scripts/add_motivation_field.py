"""
Add 'motivation' field to all incidents.
Values: 'financial' | 'political' | 'both'
- financial: primarily personal/family financial enrichment
- political: primarily political power, suppression of opposition, election advantage
- both: clearly serves both purposes
"""
import json

DATA = "c:/Users/um140/OneDrive - DN Media Group/større prosjekter/Trumps penger/data/incidents.json"

MOTIVATION_MAP = {
    "mar-a-lago-fee-increase-2025-01": "financial",
    "inauguration-fund-ambassadors-2025-01": "both",
    "trump-memecoin-launch-2025-01": "financial",
    "wlfi-uae-stake-2025-01": "financial",
    "justin-sun-sec-dropped-2025": "both",
    "trump-crypto-dinner-2025-05": "financial",
    "wlfi-usd1-binance-mgx-2025-05": "financial",
    "qatar-plane-gift-2025-05": "financial",
    "foreign-officials-trump-properties-2025": "financial",
    "liberation-day-tariff-manipulation-2025-04": "financial",
    "iran-oil-insider-trading-2026-03": "financial",
    "law-firm-coercion-2025": "political",
    "kushner-affinity-mideast-2025": "financial",
    "trump-irs-lawsuit-2026-01": "financial",
    "trump-doj-payout-230m-2025": "financial",
    "saudi-arms-trump-business-2025-05": "financial",
    "dar-global-dubai-trump-tower-2025-04": "financial",
    "melania-coin-insider-launch-2025-01": "financial",
    "fema-blue-state-denial-2025": "political",
    "ice-raids-sanctuary-cities-2025": "political",
    "inspectors-general-mass-firing-2025-01": "both",
    "npr-pbs-funding-cut-2025": "political",
    "abc-settlement-trump-library-2025": "both",
    "cbs-paramount-settlement-trump-library-2025-07": "both",
    "perkins-coie-executive-order-2025-03": "political",
    "wilmerhale-jenner-block-executive-orders-2025-03": "political",
    "harvard-funding-freeze-2025-04": "political",
    "columbia-settlement-2025-03": "political",
    "big-tech-inauguration-donations-praise-2025-01": "both",
    "meta-zuckerberg-fact-checkers-antitrust-2025-01": "both",
    "foreign-leaders-flattery-gifts-2025": "both",
    "tariff-exemptions-politically-connected-2025-04": "political",
    "trump-tech-dinner-sept-2025": "both",
    "mtg-tariff-stock-trades-2025-04": "financial",
    "pakistan-wlfi-usd1-deal-2026-01": "financial",
    "pardon-for-pay-economy-2025": "both",
    "hernandez-pardon-honduras-2025-12": "political",
    "trump-fraud-czar-hypocrisy-2026-03": "political",
    "house-gop-doral-retreat-2025-01": "financial",
    "trump-golf-taxpayer-cost-2025": "financial",
    "vietnam-golf-resort-tariff-2025-05": "financial",
    "kushner-belgrade-trump-tower-2025-11": "financial",
    "doj-ig-mass-firing-2025-01": "political",
    "military-purge-senior-officers-2025-02": "political",
    "fbi-purge-trump-investigators-2025": "political",
    "health-agency-mass-firings-2025-02": "political",
    "doj-comey-indictment-2025-09": "political",
    "doj-bolton-indictment-2025-10": "political",
    "doj-letitia-james-indictment-2025-10": "both",
    "doj-schiff-investigation-2025": "political",
    "doj-taylor-krebs-eo-2025-04": "political",
    "doj-actblue-eo-2025-04": "political",
    "doj-lisa-cook-investigation-2025": "political",
    "lawfirm-eo-perkins-coie-2025-03": "political",
    "lawfirm-paul-weiss-capitulation-2025-03": "both",
    "lawfirm-eo-jenner-wilmerhale-2025-03": "political",
    "university-funding-columbia-2025-03": "political",
    "university-funding-harvard-2025-04": "political",
    "university-funding-other-2025-04": "political",
    "media-abc-disney-settlement-2025-01": "both",
    "media-cbs-paramount-settlement-2025-07": "both",
    "media-fcc-broadcast-license-threats-2025": "political",
    "trump-nyt-lawsuit-2025-09": "political",
    "intel-chips-act-coercion-2025-08": "political",
}

with open(DATA, encoding="utf-8") as f:
    data = json.load(f)

missing = []
for inc in data["incidents"]:
    iid = inc["id"]
    if iid in MOTIVATION_MAP:
        inc["motivation"] = MOTIVATION_MAP[iid]
    else:
        inc["motivation"] = "political"  # default for any unmapped
        missing.append(iid)

with open(DATA, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

counts = {}
for inc in data["incidents"]:
    m = inc.get("motivation", "?")
    counts[m] = counts.get(m, 0) + 1

print(f"Total incidents: {len(data['incidents'])}")
print(f"Motivation breakdown: {counts}")
if missing:
    print(f"Unmapped IDs (defaulted to 'political'): {missing}")
else:
    print("All incidents mapped.")
