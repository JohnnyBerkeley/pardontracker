# Data Schema Documentation

## Incident Schema (`incidents.json`)

Each entry in the `incidents` array has the following fields:

```json
{
  "id": "string — unique slug, e.g. trump-crypto-dinner-2025-05",
  "date": "YYYY-MM-DD — date of incident or first reporting",
  "date_end": "YYYY-MM-DD — if ongoing, end date (null if still ongoing)",
  "title": "string — short descriptive title",
  "summary": "string — 2–5 sentence plain-language description",
  "categories": ["array of category codes — see below"],
  "status": "confirmed | alleged | suspected | denied",
  "beneficiary": ["array — who benefits financially"],
  "actors": ["array — people/entities involved"],
  "amount_usd": "number or null — dollar value if known",
  "amount_note": "string — explanation of amount or why it is uncertain",
  "financial_connection": {
    "exists": "boolean",
    "description": "string — how money connects to Trump or family"
  },
  "quid_pro_quo": {
    "alleged": "boolean",
    "gave": "string — what Trump/allies gave or are alleged to have given",
    "received": "string — what was received in return"
  },
  "sources": [
    {
      "title": "string",
      "url": "string",
      "date": "YYYY-MM-DD",
      "outlet": "string",
      "type": "news | official | watchdog | congressional"
    }
  ],
  "tags": ["array of freeform tags"],
  "last_updated": "YYYY-MM-DD"
}
```

## Counterparty (the organizing atom — the OTHER party in each incident)

Every incident is organized around the primary non-Trump party involved. This makes it possible to see all touchpoints with a given actor (e.g. all Saudi Arabia incidents, all Harvard incidents, all Perkins Coie incidents).

```json
"counterparty": {
  "name": "string — canonical name, e.g. 'Qatar', 'Harvard University', 'Perkins Coie LLP'",
  "type": "foreign_government | foreign_individual | domestic_company | domestic_individual | us_state | us_city | media | university | law_firm | ngo | congress_member | government_official | other",
  "country": "ISO 2-letter code or 'US'",
  "description": "one-line description of who this counterparty is"
}
```

## Categories

| Code | Description |
|------|-------------|
| `selling_access` | Payments for access to Trump or officials (Mar-a-Lago, crypto dinners, ambassador slots) |
| `pardon_financial` | Pardons with a suspected financial connection or forgiven restitution |
| `pardon_political` | Pardons with a political motive (Jan 6, allies, loyalists) |
| `crypto_sales` | Sales of $TRUMP, $MELANIA, WLFI tokens; stablecoin income |
| `business_payment` | Payments to Trump Org, hotels, golf clubs, properties |
| `family_enrichment` | Business deals benefiting Kushner, sons, Ivanka, or other family |
| `foreign_gift` | Gifts from foreign governments or state-linked entities |
| `foreign_investment` | Foreign money into Trump or family businesses/crypto |
| `insider_trading` | Suspected trading on non-public government information |
| `market_manipulation` | Alleged deliberate manipulation of markets for profit |
| `power_abuse` | Using government power to coerce, extract concessions, or punish enemies |
| `state_damages` | Claims by Trump or allies for damages from/against the government |
| `arms_deal_conflict` | Arms or policy deals where Trump business interests may influence decisions |
| `retaliation_targeting` | Entities denied something, targeted, prosecuted, defunded, or harmed specifically because they oppose Trump or his policies |
| `public_praise` | Companies, executives, or foreign leaders publicly praising Trump — especially where praise coincides with receiving or seeking favorable treatment, exemptions, regulatory relief, or policy concessions |

## Beneficiary Codes

- `trump_personally` — Trump himself
- `trump_org` — Trump Organization
- `trump_family` — Family members (specify in actors)
- `kushner` — Jared Kushner / Affinity Partners
- `trump_pac` — Trump PACs or political committees
- `trump_crypto` — Fight Fight Fight LLC / WLFI / crypto entities

## Pardon Schema (`pardons.json`)

```json
{
  "id": "string",
  "name": "string — full name of recipient",
  "date": "YYYY-MM-DD",
  "type": "pardon | commutation | mass_pardon",
  "group": "string — e.g. 'January 6', 'Fake Electors', or null",
  "offense": "string — what they were convicted/charged with",
  "original_sentence": "string",
  "fines_forgiven_usd": "number or null",
  "restitution_forgiven_usd": "number or null",
  "restitution_owed_to": "private_victims | government | both | null",
  "financial_connection": {
    "exists": "boolean",
    "description": "string"
  },
  "political_connection": {
    "exists": "boolean",
    "description": "string"
  },
  "sources": ["array of source objects — same format as incidents"],
  "notes": "string"
}
```
