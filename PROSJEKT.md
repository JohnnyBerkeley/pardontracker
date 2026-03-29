# Trump Money Map — Prosjektoversikt

## Hva er dette?
Et strukturert datasett og visualiseringsprosjekt som kartlegger pengeflyt, korrupsjon og maktmisbruk knyttet til Donald Trump og hans familie under hans andre presidentperiode (20. januar 2025–).

## Filstruktur

```
data/
  schema.md          — Full dokumentasjon av datastruktur og kategorier
  incidents.json     — Alle hendelser (korrupsjon, maktmisbruk, pengeflyt)
  pardons.json       — Full liste over benadigninger og straffefritak
scripts/
  update_search.py   — Søkeoppdateringsscript (kjør for å finne nye saker)
```

## Kategorier (incidents.json)

| Kode | Norsk beskrivelse |
|------|-------------------|
| `selling_access` | Betaling for tilgang til Trump (Mar-a-Lago, kryptomiddager) |
| `pardon_financial` | Benadigninger med finansiell kobling |
| `pardon_political` | Politisk motiverte benadigninger (Jan 6 etc.) |
| `crypto_sales` | Salg av $TRUMP, $MELANIA, WLFI-tokens, stablecoin |
| `business_payment` | Betalinger til Trump Org, hoteller, golfklubber |
| `family_enrichment` | Kushner, sønner, Ivanka — familieberikelse |
| `foreign_gift` | Gaver fra utenlandske myndigheter |
| `foreign_investment` | Utenlandske penger inn i Trump/familie-bedrifter |
| `insider_trading` | Mistanke om handel på ikke-offentlig informasjon |
| `market_manipulation` | Påstått manipulasjon av markedet for profitt |
| `power_abuse` | Bruk av statsmakt for å presse/straffe/belønne |
| `state_damages` | Krav om erstatning fra staten |
| `arms_deal_conflict` | Våpenhandel der Trump har private interesser |
| `retaliation_targeting` | Stater/universiteter/firmaer straffet for å motarbeide Trump |
| `public_praise` | Offentlig ros av Trump sammenfaller med å motta fordeler |

## Datafangst-strategi

### Engangspull (gjort 2026-03-28)
Dekker perioden 2025-01-20 til 2026-03-28. Søkte på tvers av alle kategorier.

### Oppdateringer
Kjør `python scripts/update_search.py` for å få søkespørringer du skal kjøre manuelt eller i Claude Code. Scriptet bruker `last_updated`-datoen i `incidents.json` som startpunkt.

**Anbefalte kilder å overvåke ukentlig:**
- [CREW](https://www.citizensforethics.org/) — konflikter og emoluments
- [ProPublica](https://www.propublica.org/topics/trump) — undersøkende journalistikk
- [DOJ Pardon Attorney](https://www.justice.gov/pardon/clemency-grants-president-donald-j-trump-2025-present) — offisiell benadigningsliste
- [American Oversight](https://americanoversight.org/tracking-taxpayer-spending-at-trump-properties/) — statlig pengebruk på Trump-eiendom
- [OpenSecrets](https://www.opensecrets.org/) — kampanjefinansiering

## Datasett-status (per 2026-03-28)

| Fil | Antall poster | Sist oppdatert |
|-----|--------------|----------------|
| `incidents.json` | 36 hendelser | 2026-03-28 |
| `pardons.json` | 46 benadigninger | 2026-03-28 |

**Benadigninger — sporede summer:**
- Bøter frafalt: $351M
- Erstatning frafalt: $880M
- **Totalt sporet: $1,23 milliarder** (CA-guvernør estimerer ~$2B totalt)
- Finansiell kobling: 8 benadigninger
- Politisk kobling: 33 benadigninger

## Viktige funn (per 2026-03-28)

### Crypto-imperium (~$20B+)
- $TRUMP memecoin: Trump tjener direkte når noen kjøper mynten
- World Liberty Financial: UAE-kongefamilien eier 49% ($500M), $187M gikk til Trump-family LLC-er
- CZ Zhao (Binance) fikk benådning etter å ha bygget WLFI-infrastruktur
- Justin Sun (kinesisk milliardær): investerte $75M i Trump-krypto, SEC-sak ble droppet

### Utenlandske gaver og emoluments
- Qatar-fly: Boeing 747-8 verdt $400M+ mottatt fra Qatar; USA skal bruke $400M til til å bygge det om
- 55 utenlandske tjenestemenn fra 21 land besøkte Trump-eiendommer i år 1
- Saudi-Arabias LIV Golf-turneringer på Trump Doral

### Insider trading / markedsmanipulasjon
- «Liberation Day» (2. april 2025): $5 billioner forsvant fra markeder; 9. april snudde Trump, markeder slo rekord
- Iran-oljehandel (24. mars 2026): $580M i oljekontrakter solgt 16 minutter FØR Trumps Truth Social-innlegg

### Maktmisbruk
- Advokatfirmaer: $1,2 milliarder tvunget ut i gratisarbeid
- Universiteter: $1 milliard i oppgjør (bl.a. UCLA)

### Kushner
- Affinity Partners: $6,2 milliarder i forvaltede midler; Saudi PIF investerte $2 milliarder
- Søker $5 milliarder fra Gulf-regjeringer MENS han er Trumps utsending til regionen

### Erstatningskrav mot staten
- $10 milliarder søksmål mot IRS/Treasury (Trump saksøker sine egne etater)
- $230 millioner krav mot DOJ

### Benadigninger (finansielle koblinger)
- Trevor Milton: $661M erstatning til private ofre frafalt (donerte $1,8M til Trump-kampanjen)
- Paul Walczak: $4,4M frafalt (mor donerte $1M til MAGA Inc.)
- Todd + Julie Chrisley: $22,5M frafalt (politisk støtte, lobbyist)
- CZ Zhao: $50M bot frafalt (kripto-forretningsforbindelser)
- Adriana + Andres Camberos: $97,6M erstatning frafalt (jan 2026)
- Terren Peizer: $17,95M (bot + forbehold) frafalt (jan 2026, insider trading)
- ~1.500 Jan 6-deltakere: politisk benådning
- 77 falske valgmenn m.fl. (Giuliani, Meadows, Powell, Eastman m.fl.): nov 2025
- Larry Hoover: 6 livstidsdommer omgjort til tid tjent (mai 2025)
- 5 NFL-spillere: frafalt pga sport-PR (feb 2026)
- «Fortunate sons»: James Womack (sønn av kongressmann), Jacob Deutsch (jan 2026)
- Wanda Vázquez Garced (PR-guvernør som støttet Trump 2020) + medtiltalte: jan 2026

### Benadigningsøkonomi
- Standard lobbyisthonorar: $1M; suksesshonorar opptil $6M
- Herrera Velutini: $3,5M til Trump-PAC → benådning
- Schwartz: $1,1M i lobbyisthonorar → benådning
- Leiweke: golfbane-lobbying via Trey Gowdy → benådning

## Neste steg
1. Bygg webvisualisering (anbefalt: SvelteKit + D3.js, eller Observable Framework)
2. Legg til flere hendelser (Al-Qaeda-pengeflyt via Binance, Eric Trump Dubai-avtale, etc.)
3. Legg til 50+ kongressmedlemmers aksjehandler (utover MTG)
4. Legg til detaljer om utenlandske statsbesøk og hotellbetalinger (Modi, Ishiba)
5. Sett opp ukentlig overvåking av kildene over
