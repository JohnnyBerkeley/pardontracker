# Trump Money Map — Editorial Rules & Data Standards

This document encodes the editorial judgment rules used to decide what goes
into this dataset, how to classify it, and how to describe it. It is the
"institutional memory" of the project. When a new Claude session starts, this
document (plus `data/schema.md`) should be read to restore full context.

---

## Purpose of the Dataset

Track financial conflicts of interest, power abuse, and related misconduct by
Donald Trump and his administration during the second presidency (Jan 20,
2025–). The counterparty (the other party in each incident — not Trump) is
the organizing unit, so all incidents involving the same actor can be grouped.

The dataset is journalistic, not prosecutorial. It records *documented*
incidents, flags what is *alleged* vs *confirmed*, and never claims guilt
beyond what sources support.

---

## What Qualifies for Inclusion

An incident must meet at least one of:

1. **Documented money flow** to Trump, his family, or associated entities that
   appears linked to a government decision, action, or omission.
2. **Documented government action** (contract, loan, regulatory relief,
   pardon, dropped charge, policy change) that benefits an entity with a
   financial relationship to Trump or family.
3. **Documented coercion or threat** where the administration used or implied
   government power to extract financial or political concessions.
4. **Documented firing, prosecution, or targeting** of a person or institution
   where political motivation is either confirmed (Trump stated it) or strongly
   supported by evidence (timing, pattern, prior statements).
5. **Constitutional violation** where a court has found or legal experts
   broadly agree an action violates a specific constitutional provision.

**Do not include:**
- Pure policy disagreements with no personal financial or retaliatory dimension
- Allegations based solely on anonymous sources with no corroboration
- Incidents already covered by an existing entry (update the existing one)

---

## Source Standards

**Acceptable primary sources:**
- Major US and international news organizations (NYT, WaPo, WSJ, Reuters, AP,
  Bloomberg, FT, Politico, CNN, NPR, CNBC, BBC)
- Court filings, government documents, official DOJ/SEC/FEC records
- Congressional testimony and official letters
- Watchdog organizations: CREW, POGO, Democracy Forward, OpenSecrets
- Academic or legal analysis from named experts at named institutions

**Use with caution:**
- Single-source reports on sensitive claims — flag as `alleged`
- Partisan outlets — verify with independent source before `confirmed`
- Social media posts by subjects — useful as evidence of intent/statements

**Required minimum:** Every incident needs at least one source URL. Prefer
sources that are freely accessible (not paywalled) where possible.

---

## Status Field Rules

Use exactly one of: `confirmed`, `alleged`, `suspected`, `denied`

| Status | Use when |
|---|---|
| `confirmed` | The fact is documented by at least two independent credible sources, OR there is official record (court filing, government document, Trump's own public statement) |
| `alleged` | Credible reporting but not yet independently confirmed, OR a single strong source, OR the political motivation is inferred from strong circumstantial evidence |
| `suspected` | Pattern-based inference from multiple data points but no direct evidence; watchdog organizations have flagged it |
| `denied` | Trump or administration has explicitly denied and there is no strong counter-evidence |

**Key rule:** Trump's own Truth Social posts, press conference statements, and
signed executive orders are primary sources that can support `confirmed`.
When Trump publicly demands a prosecution and the DOJ acts, that sequence
supports `confirmed` status for the targeting allegation.

---

## Motivation Field Rules

Use exactly one of: `financial`, `political`, `both`

| Value | Use when |
|---|---|
| `financial` | The primary identifiable benefit is money flowing to Trump, family, or associated businesses. Political gain is secondary or absent. |
| `political` | The primary identifiable benefit is political: suppressing opposition, rewarding loyalty, winning future elections, consolidating power. No direct personal financial gain. |
| `both` | The incident clearly serves both — e.g., media settlements that pay Trump's library AND silence critical coverage; pardons of donors who also helped politically. |

**Default toward `both` when genuinely uncertain** rather than forcing a
single classification.

---

## Category Assignment Rules

An incident can have multiple categories. Assign all that clearly apply.
Do not over-categorize — only include a category if it is substantively
present, not just tangentially related.

| Category | Assign when |
|---|---|
| `selling_access` | Someone paid money (membership fee, donation, event ticket) and in exchange gained physical or policy proximity to Trump |
| `crypto_sales` | Revenue from $TRUMP, $MELANIA, WLFI tokens, USD1 stablecoin, or related crypto ventures |
| `business_payment` | Direct payment to Trump Organization, hotels, golf clubs, or Trump-owned properties |
| `family_enrichment` | Business deals that benefit Kushner, Eric, Don Jr., Ivanka, or other family members through their private businesses |
| `foreign_investment` | Foreign government money or state-linked money flowing into Trump or family businesses |
| `foreign_gift` | A gift of monetary value from a foreign government or official (Qatar plane, etc.) |
| `insider_trading` | Evidence that a Trump-linked person traded on non-public government information |
| `market_manipulation` | Evidence of deliberate market-moving action for profit (tariff announcement/reversal patterns) |
| `power_abuse` | Government power used to coerce, extract, punish, or enrich beyond legal authority |
| `retaliation_targeting` | A person or institution was prosecuted, fired, defunded, or harmed *specifically because* they opposed Trump or were in his way |
| `public_praise` | A company or individual publicly praised Trump, where the praise coincides with receiving or seeking favorable government treatment |
| `pardon_financial` | A pardon where there is a documented or alleged financial connection to Trump (donor, crypto partner, business relationship) |
| `pardon_political` | A pardon with a clear political motive (ally, Jan 6 participant, someone who praised Trump, political enemy of a political enemy) |
| `state_damages` | Trump or associated entities filing claims against the US government itself for money |
| `arms_deal_conflict` | An arms deal or military contract where Trump business interests may have influenced the decision |
| `coercion_threat` | The administration threatened a business, university, or media organization with regulatory, legal, or funding consequences unless they complied with political demands |
| `investment_favoritism` | Trump or family held an investment in a company that then received government contracts, loans, favorable regulations, or approvals in a pattern suggesting self-enrichment |

---

## Financial Connection Assessment

For `financial_connection.exists`, use:
- `true` — there is a documented, traceable money link (contract, fee, equity,
  donation, forgiven fine, settlement payment)
- `false` — investigation found no financial link
- `null` — unknown; not yet investigated

The `description` field should explain the mechanism: *how* the money moves,
*to whom*, and *why it is suspicious* (not just that it exists).

---

## Quid Pro Quo Assessment

`quid_pro_quo.alleged` should be `true` when:
- There is a documented exchange: something given, something received
- The timing is suspicious (donation → regulatory relief → policy change)
- Both parties acknowledge the relationship even if denying impropriety

The `gave` and `received` fields should be concrete and specific, not vague.
Bad: "gave access, received money." Good: "Gave: $500K Mar-a-Lago initiation
fee. Received: physical access to sitting president at social events."

---

## Counterparty Model

Every incident is organized around the primary non-Trump party. This allows
grouping all incidents involving a given actor. Rules:

- Use the most specific name possible (not "a Saudi investor" but "Saudi
  Public Investment Fund" or the individual's name)
- `type` must be one of the defined types in schema.md
- `country` is ISO 2-letter code or `US`
- `description` is one line explaining who this party is and why they matter

---

## Duplicate Prevention

Before adding a new incident, check if an existing entry covers it:
- Search by counterparty name
- Search by date range and category
- Check if it is a follow-up to an existing incident (update the existing one,
  don't create a duplicate)

If a new development significantly changes an existing incident (charges
dropped, settlement reached, court ruling), update the existing entry rather
than creating a new one. Update `last_updated` and add to the summary.

---

## Threshold for Inclusion

**Include:** A $40,000 fine forgiven in a pardon. A $75M university settlement.
A $10M drone contract to a company Trump Jr. invested in last month.

**Do not include:** General policy decisions (cutting EPA regulations) without
a traceable personal financial link. Rhetorical statements without follow-up
action. Stories covered only by advocacy sites with no independent verification.

**Gray area → `alleged`:** If a story is credible but the financial link is
circumstantial, include it as `alleged` with a clear description of what is
known and what is inferred.

---

## Pardons — Special Rules

Every pardon entry should document:
1. What the person was convicted of (specific offense, not vague)
2. The exact dollar amount forgiven (fines + restitution separately)
3. Who the restitution was owed to: `private_victims`, `government`, or `both`
4. Whether there is a financial connection to Trump (donation, business
   relationship, crypto partner)
5. Whether there is a political connection (ally, Jan 6 participant, person
   who publicly praised Trump, person connected to a Trump enemy)

For mass pardons (Jan 6, fake electors), create one group entry with a count
and description rather than individual entries unless specific individuals have
notable financial amounts or connections.

---

## Constitutional Violations — Special Rules

Track in `constitutional_violations.json` (separate from incidents).
Include only when:
- A court has actually ruled, OR
- Multiple credible legal scholars/organizations have identified a specific
  constitutional provision and explained *why* it is violated

Always name the specific amendment(s) or constitutional clause(s).
Always name who is making the claim (courts, ACLU, specific scholars).
Use the `status` field strictly: `court_blocked`, `ruled_unconstitutional`,
`supreme_court_ruled_illegal`, `pending`, `alleged`.

---

## Language and Tone

- Factual, not editorializing
- Use hedge words where appropriate: "alleged," "suspected," "critics argue"
- Do not say "Trump committed fraud" — say "Trump was found liable for fraud
  in a civil case (verdict: Feb 2024)"
- For `alleged` items, always attribute: "according to [source]" or
  "prosecutors alleged"
- Titles should be descriptive, not sensational: describe what happened, not
  what it proves

---

## Update Workflow

When adding new incidents (via URL, article paste, or periodic search):

1. Check against this document: does it qualify?
2. Check for duplicates in existing data
3. Assign category, status, motivation
4. Find and cite at least one source URL
5. Set `financial_connection.exists` and describe the mechanism
6. Set `quid_pro_quo.alleged` and fill `gave`/`received` if applicable
7. Set `last_updated` to today's date
8. Rebuild `index.html` after adding: `python scripts/build_html.py`
9. Commit to git

---

*Document version: 2026-03-30. Update this document when new categories are
added, rules are refined, or editorial standards change.*
