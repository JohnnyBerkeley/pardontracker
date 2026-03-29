import json

DATA = "c:/Users/um140/OneDrive - DN Media Group/større prosjekter/Trumps penger/data/pardons.json"

with open(DATA, encoding="utf-8") as f:
    data = json.load(f)

pardons = data["pardons"]

new_entries = [
    {
      "id": "arthur-hayes-2025-03",
      "name": "Arthur Hayes",
      "date": "2025-03-28",
      "type": "pardon",
      "group": "BitMEX founders",
      "offense": "Bank Secrecy Act violation — failure to implement anti-money laundering program at BitMEX crypto exchange (pleaded guilty 2022)",
      "original_sentence": "Probation; $10,000,000 fine",
      "fines_forgiven_usd": 10000000,
      "restitution_forgiven_usd": None,
      "restitution_owed_to": "government",
      "financial_connection": {"exists": None, "description": "Crypto industry figure; fits Trump's broader crypto deregulation agenda"},
      "political_connection": {"exists": True, "description": "Part of Trump's crypto industry pardons batch; BitMEX parent company separately fined $100M"},
      "sources": [{"title": "Trump Pardons Bitmex Co-Founders Arthur Hayes, Benjamin Delo and Samuel Reed", "url": "https://www.bloomberg.com/news/articles/2025-03-28/trump-pardons-bitmex-co-founders-arthur-hayes-benjamin-delo-and-samuel-reed", "date": "2025-03-28", "outlet": "Bloomberg", "type": "news"}],
      "notes": "$10M fine forgiven. Co-founder of BitMEX exchange."
    },
    {
      "id": "benjamin-delo-2025-03",
      "name": "Benjamin Delo",
      "date": "2025-03-28",
      "type": "pardon",
      "group": "BitMEX founders",
      "offense": "Bank Secrecy Act violation — failure to implement anti-money laundering program at BitMEX (pleaded guilty 2022)",
      "original_sentence": "Probation; $10,000,000 fine",
      "fines_forgiven_usd": 10000000,
      "restitution_forgiven_usd": None,
      "restitution_owed_to": "government",
      "financial_connection": {"exists": None, "description": "Crypto industry figure"},
      "political_connection": {"exists": True, "description": "Part of Trump's crypto industry pardons batch"},
      "sources": [{"title": "Trump Pardons Bitmex Co-Founders Arthur Hayes, Benjamin Delo and Samuel Reed", "url": "https://www.bloomberg.com/news/articles/2025-03-28/trump-pardons-bitmex-co-founders-arthur-hayes-benjamin-delo-and-samuel-reed", "date": "2025-03-28", "outlet": "Bloomberg", "type": "news"}],
      "notes": "$10M fine forgiven. Co-founder of BitMEX exchange."
    },
    {
      "id": "samuel-reed-2025-03",
      "name": "Samuel Reed",
      "date": "2025-03-28",
      "type": "pardon",
      "group": "BitMEX founders",
      "offense": "Bank Secrecy Act violation — failure to implement anti-money laundering program at BitMEX (pleaded guilty 2022)",
      "original_sentence": "Probation; $10,000,000 fine",
      "fines_forgiven_usd": 10000000,
      "restitution_forgiven_usd": None,
      "restitution_owed_to": "government",
      "financial_connection": {"exists": None, "description": "Crypto industry figure"},
      "political_connection": {"exists": True, "description": "Part of Trump's crypto industry pardons batch"},
      "sources": [{"title": "Trump Pardons Bitmex Co-Founders Arthur Hayes, Benjamin Delo and Samuel Reed", "url": "https://www.bloomberg.com/news/articles/2025-03-28/trump-pardons-bitmex-co-founders-arthur-hayes-benjamin-delo-and-samuel-reed", "date": "2025-03-28", "outlet": "Bloomberg", "type": "news"}],
      "notes": "$10M fine forgiven. Co-founder of BitMEX exchange."
    },
    {
      "id": "gregory-dwyer-2025-03",
      "name": "Gregory Dwyer",
      "date": "2025-03-28",
      "type": "pardon",
      "group": "BitMEX founders",
      "offense": "Bank Secrecy Act violation — former head of business development at BitMEX (pleaded guilty)",
      "original_sentence": "12 months probation; $150,000 fine",
      "fines_forgiven_usd": 150000,
      "restitution_forgiven_usd": None,
      "restitution_owed_to": "government",
      "financial_connection": {"exists": None, "description": "Crypto industry figure"},
      "political_connection": {"exists": True, "description": "Part of Trump's crypto industry pardons batch"},
      "sources": [{"title": "Trump pardons three BitMEX crypto exchange co-founders, and ex-employee", "url": "https://www.cnbc.com/2025/03/28/trump-pardon-bitmex-crypto-exchange-money-laundering.html", "date": "2025-03-28", "outlet": "CNBC", "type": "news"}],
      "notes": "$150K fine forgiven. Former head of business development at BitMEX."
    },
    {
      "id": "jason-galanis-2025-03",
      "name": "Jason Galanis",
      "date": "2025-03-28",
      "type": "commutation",
      "group": None,
      "offense": "Securities fraud and investment adviser fraud — orchestrated $60M fraud against the Oglala Sioux Nation (fake tribal bonds); separately convicted of investment adviser fraud. Called a 'serial fraudster' by House Judiciary Democrats.",
      "original_sentence": "189 months (14 years) imprisonment; $84,817,513.43 restitution across two court judgments",
      "fines_forgiven_usd": None,
      "restitution_forgiven_usd": 84817513,
      "restitution_owed_to": "private_victims",
      "financial_connection": {"exists": False, "description": "No direct Trump financial connection"},
      "political_connection": {"exists": True, "description": "Former business associate of Hunter Biden. Testified from prison to Republican congressional investigators. Trump framed commutation as correcting Biden-era prosecution. Devon Archer (co-defendant) also pardoned same day."},
      "sources": [
        {"title": "Trump commutes prison sentence of Hunter Biden's 'fall guy' Jason Galanis", "url": "https://www.foxnews.com/politics/trump-commutes-prison-sentence-hunter-bidens-fall-guy-jason-galanis", "date": "2025-04-01", "outlet": "Fox News", "type": "news"},
        {"title": "Trump commutes sentence of second man convicted in $60M Oglala Sioux fraud case", "url": "https://tribalbusinessnews.com/sections/policy-and-law/15074-trump-commutes-sentence-of-second-man-convicted-in-60m-oglala-sioux-fraud-case", "date": "2025-04-01", "outlet": "Tribal Business News", "type": "news"}
      ],
      "notes": "$84,817,513.43 restitution wiped — owed to Oglala Sioux Nation and investment fraud victims. Framed by Trump as correcting Biden-era persecution. Native American tribal victims will not be compensated."
    },
    {
      "id": "imaad-shah-zuberi-2025-05",
      "name": "Imaad Shah Zuberi",
      "date": "2025-05-28",
      "type": "commutation",
      "group": None,
      "offense": "Illegal campaign contributions, falsifying foreign lobbying records (FARA violations), tax evasion, obstruction of justice",
      "original_sentence": "12 years imprisonment; $15,705,080.11 restitution; $1,750,000 fine",
      "fines_forgiven_usd": 1750000,
      "restitution_forgiven_usd": 15705080,
      "restitution_owed_to": "government",
      "financial_connection": {"exists": True, "description": "Donated $900K to Trump's 2016 inaugural committee. Illegal contributions included foreign money funneled into US campaigns."},
      "political_connection": {"exists": True, "description": "American-Pakistani venture capitalist and political mega-donor; donated $900K to Trump's 2016 inauguration. Also donated to Democratic campaigns."},
      "sources": [
        {"title": "Trump commutes sentence for donor Imaad Zuberi", "url": "https://www.newsnationnow.com/politics/trump-commutes-sentence-for-donor-imaad-zuberi/", "date": "2025-05-29", "outlet": "NewsNation", "type": "news"}
      ],
      "notes": "Donated $900K to Trump's 2016 inaugural committee. Convicted of FARA violations and illegal foreign campaign contributions. $15.7M restitution + $1.75M fine wiped."
    },
    {
      "id": "marian-morgan-2025-05",
      "name": "Marian Isabella Morgan",
      "date": "2025-05-28",
      "type": "commutation",
      "group": None,
      "offense": "Conspiracy to defraud United States, wire fraud (7 counts), money laundering (6 counts), false tax returns — defrauded 87 people of $28 million",
      "original_sentence": "35 years imprisonment; $19,958,995 restitution",
      "fines_forgiven_usd": None,
      "restitution_forgiven_usd": 19958995,
      "restitution_owed_to": "private_victims",
      "financial_connection": {"exists": False, "description": "No direct Trump financial connection identified"},
      "political_connection": {"exists": False, "description": "No identified political connection in public reporting"},
      "sources": [
        {"title": "2025-05-28 Commutation MARIAN ISABELLA MORGAN", "url": "https://www.justice.gov/pardon/media/1402051/dl?inline=", "date": "2025-05-28", "outlet": "DOJ Office of Pardon Attorney", "type": "official"}
      ],
      "notes": "Received 35-year sentence for defrauding 87 private victims of $28M. Commutation wipes $19,958,995 in restitution owed to private fraud victims."
    },
    {
      "id": "pg-sittenfeld-2025-05",
      "name": "P.G. Sittenfeld (Alexander Sittenfeld)",
      "date": "2025-05-29",
      "type": "pardon",
      "group": None,
      "offense": "Bribery and attempted extortion — as Cincinnati City Councilman, accepted $20,000 in PAC donations in exchange for promising votes on a real estate development project with sports betting",
      "original_sentence": "16 months imprisonment",
      "fines_forgiven_usd": 40000,
      "restitution_forgiven_usd": None,
      "restitution_owed_to": "government",
      "financial_connection": {"exists": False, "description": "No direct Trump financial connection"},
      "political_connection": {"exists": True, "description": "Democratic city councilman — unusual Trump pardon of a Democrat. Former US Attorney called the pardon undermining of legitimate anti-corruption work."},
      "sources": [
        {"title": "Trump pardons PG Sittenfeld, ex-Cincinnati councilman convicted of bribery", "url": "https://www.yahoo.com/news/trump-pardons-pg-sittenfeld-ex-124034229.html", "date": "2025-05-29", "outlet": "Yahoo News", "type": "news"}
      ],
      "notes": "Democrat pardoned — unusual. $40K in fines forgiven."
    },
    {
      "id": "david-gentile-2025-12",
      "name": "David Gentile",
      "date": "2025-12-01",
      "type": "commutation",
      "group": None,
      "offense": "Investment fraud — Ponzi scheme that defrauded ~17,000 investors of $1.6 billion (GPB Capital); faked financial statements, misrepresented how investor distributions were funded",
      "original_sentence": "7 years imprisonment; $15,500,000 restitution to victims",
      "fines_forgiven_usd": None,
      "restitution_forgiven_usd": 15500000,
      "restitution_owed_to": "private_victims",
      "financial_connection": {"exists": None, "description": "No direct Trump financial connection publicly established; Senate Democrats demanded answers"},
      "political_connection": {"exists": False, "description": "Private equity CEO (GPB Capital). No clear political connection identified."},
      "sources": [
        {"title": "Trump commutes sentence of private equity CEO convicted of fraud", "url": "https://www.cnn.com/2025/12/01/politics/david-gentile-trump-pardon", "date": "2025-12-01", "outlet": "CNN", "type": "news"},
        {"title": "Gallego Leads Colleagues in Demanding Answers Over Trump's Commutation of Convicted Fraudster David Gentile", "url": "https://www.gallego.senate.gov/news/press-releases/gallego-leads-colleagues-in-demanding-answers-over-trumps-pardon-of-convicted-fraudster-david-gentile/", "date": "2025-12-10", "outlet": "US Senate", "type": "congressional"}
      ],
      "notes": "Served only 12 days of 7-year sentence before commuted. Defrauded 17,000 investors of $1.6B. $15.5M in victim restitution wiped. Senate Democrats demanded explanation; none given publicly."
    }
]

# Replace bitmex-founders group entry with individual entries
idx = next(i for i, p in enumerate(pardons) if p["id"] == "bitmex-founders-2025-03")
pardons[idx:idx+1] = new_entries

data["pardons"] = pardons

with open(DATA, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

total_fines = sum(p.get("fines_forgiven_usd") or 0 for p in pardons)
total_res = sum(p.get("restitution_forgiven_usd") or 0 for p in pardons)
print(f"Total pardons: {len(pardons)}")
print(f"Fines/forfeitures forgiven: ${total_fines:,.0f}")
print(f"Restitution forgiven: ${total_res:,.0f}")
print(f"Grand total: ${total_fines + total_res:,.0f}")
