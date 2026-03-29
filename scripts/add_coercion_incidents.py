"""
Add coercion/threat incidents where Trump or his admin threatened businesses,
universities, or media companies unless they complied with political demands.
New category: coercion_threat
"""
import json

DATA = "c:/Users/um140/OneDrive - DN Media Group/større prosjekter/Trumps penger/data/incidents.json"

with open(DATA, encoding="utf-8") as f:
    data = json.load(f)

incidents = data["incidents"]

new_incidents = [
    {
        "id": "lawfirm-eo-perkins-coie-2025-03",
        "date": "2025-03-06",
        "date_end": "2025-05-02",
        "title": "Trump EO targets Perkins Coie — suspends clearances, bars federal access",
        "summary": "On March 6, 2025, Trump signed Executive Order 14230 targeting Perkins Coie, a law firm that had represented Hillary Clinton's 2016 campaign and other Democratic clients. The EO suspended all employee security clearances, barred firm members from entering federal buildings, and directed federal agencies to terminate all government contracts with the firm. The stated reason was the firm's association with the Steele dossier. The actual effect was to destroy the firm's ability to represent any client with federal regulatory exposure. Perkins Coie sued immediately. On May 2, 2025, a federal judge permanently blocked the order as 'an unprecedented attack' on the legal system, calling it 'null and void.' The DOJ later moved to drop its defense of the order.",
        "categories": ["coercion_threat", "power_abuse", "retaliation_targeting"],
        "status": "confirmed",
        "counterparty": {
            "name": "Perkins Coie",
            "type": "organization",
            "country": "US",
            "description": "Major law firm; represented Clinton 2016 campaign and other Democratic clients; blocked by EO 14230"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "White House Counsel's Office"],
        "amount_usd": None,
        "amount_note": "Loss of government contracts; cost to firm's reputation and clients' cases — not quantified publicly",
        "financial_connection": {
            "exists": False,
            "description": "No direct Trump financial benefit. Retaliation for the firm's prior work on cases adverse to Trump."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Destroyed firm's ability to work on federal matters",
            "received": "Retaliation against a firm that worked against Trump; deterrence for other firms"
        },
        "tags": ["law_firm", "executive_order", "coercion", "security_clearances", "court_blocked"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Judge strikes down Trump's executive order targeting law firm Perkins Coie",
                "url": "https://www.aljazeera.com/news/2025/5/3/judge-strikes-down-trumps-executive-order-targeting-law-firm-perkins-coie",
                "date": "2025-05-03",
                "outlet": "Al Jazeera",
                "type": "news"
            },
            {
                "title": "Trump's executive orders against law firms",
                "url": "https://firstamendment.mtsu.edu/article/trumps-executive-orders-against-law-firms/",
                "date": "2025-06-01",
                "outlet": "First Amendment Encyclopedia / MTSU",
                "type": "analysis"
            }
        ]
    },
    {
        "id": "lawfirm-paul-weiss-capitulation-2025-03",
        "date": "2025-03-14",
        "date_end": "2025-03-21",
        "title": "Paul Weiss capitulates to Trump — pledges $40M pro bono, ends DEI",
        "summary": "On March 14, 2025, Trump signed Executive Order 14237 targeting Paul Weiss, a prominent law firm. The EO suspended security clearances, barred federal building access, and directed contract terminations. The trigger was attorney Mark Pomerantz, a former Paul Weiss partner who had joined the Manhattan DA's office to help prosecute Trump. Rather than sue — as other firms did — Paul Weiss capitulated within a week. The firm pledged $40 million in pro bono work exclusively for Trump-approved causes (veterans, combating antisemitism), agreed to review and end DEI practices, and acknowledged the administration's concerns. Trump rescinded the EO on March 21. Legal commentators called it 'humiliating capitulation' and noted it set a precedent for the government coercing private firms through threat of debarment. Eight other major firms — Skadden, Milbank, Willkie Farr, Cadwalader, Kirkland & Ellis, A&O Shearman, Latham & Watkins, Simpson Thacher — made preemptive deals to avoid similar EOs, collectively pledging nearly $940 million in pro bono work for administration-approved causes.",
        "categories": ["coercion_threat", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "Paul Weiss / Major US law firms",
            "type": "organization",
            "country": "US",
            "description": "Paul Weiss + 8 other firms (Skadden, Milbank, Willkie Farr, Cadwalader, Kirkland & Ellis, A&O Shearman, Latham & Watkins, Simpson Thacher) collectively pledged ~$940M in pro bono for Trump-approved causes"
        },
        "beneficiary": ["trump_personally", "trump_allies"],
        "actors": ["Donald Trump", "White House Counsel's Office"],
        "amount_usd": 940000000,
        "amount_note": "Estimated $940M total pro bono pledges across 9 settling firms (Paul Weiss $40M + 8 others at $100-125M each)",
        "financial_connection": {
            "exists": True,
            "description": "Pro bono work directed by Trump to his preferred causes ($940M total). Firms gained relief from EOs that would have destroyed their federal business."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": "End DEI practices; pledge pro bono for Trump-approved causes; distance from anti-Trump attorneys",
            "received": "Rescission of EO / no EO issued; ability to continue federal government work"
        },
        "tags": ["law_firm", "executive_order", "coercion", "pro_bono", "dei", "capitulation"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump rescinds executive order that targeted Paul Weiss law firm",
                "url": "https://news.bloomberglaw.com/business-and-practice/trump-rescinds-executive-order-that-targeted-paul-weiss-law-firm",
                "date": "2025-03-21",
                "outlet": "Bloomberg Law",
                "type": "news"
            },
            {
                "title": "Paul Weiss executive order rescinded — White House statement",
                "url": "https://www.cbsnews.com/news/paul-weiss-executive-order-rescinded-white-house-trump/",
                "date": "2025-03-21",
                "outlet": "CBS News",
                "type": "news"
            },
            {
                "title": "Milbank signs deal with Trump to avoid executive order",
                "url": "https://news.bloomberglaw.com/business-and-practice/milbank-signs-deal-with-trump-to-avoid-executive-order",
                "date": "2025-03-28",
                "outlet": "Bloomberg Law",
                "type": "news"
            }
        ]
    },
    {
        "id": "lawfirm-eo-jenner-wilmerhale-2025-03",
        "date": "2025-03-25",
        "date_end": "2025-05-27",
        "title": "Trump EOs target Jenner & Block, WilmerHale — both struck down as unconstitutional",
        "summary": "Trump signed Executive Order 14246 (March 25, 2025) targeting Jenner & Block — citing attorney Andrew Weissmann's work on the Mueller investigation — and Executive Order 14250 (March 27, 2025) targeting WilmerHale, which had employed Robert Mueller and represented the DNC and Biden/Harris campaigns. Both orders suspended security clearances, barred federal access, and directed contract terminations. Both firms sued immediately. Jenner & Block: Judge Bates issued an immediate TRO; on May 23, 2025 declared the EO unconstitutional as it 'seeks to chill legal representation the administration doesn't like.' WilmerHale: federal judge struck down the EO on May 27, 2025. The DOJ dropped its appeals in both cases. A presidential memorandum had earlier (February 25, 2025) targeted Covington & Burling over its attorneys' work for Jack Smith's special counsel investigation.",
        "categories": ["coercion_threat", "power_abuse", "retaliation_targeting"],
        "status": "confirmed",
        "counterparty": {
            "name": "Jenner & Block / WilmerHale / Covington & Burling",
            "type": "organization",
            "country": "US",
            "description": "Three firms targeted for employing attorneys who worked on Trump investigations (Mueller, Jack Smith). All EOs/memo struck down or challenged."
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "White House Counsel's Office"],
        "amount_usd": None,
        "amount_note": "Significant legal costs for all three firms to defend themselves; temporary loss of federal business",
        "financial_connection": {
            "exists": False,
            "description": "No direct Trump financial benefit. Retaliation for firms employing prosecutors who investigated Trump."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Suspension of ability to do federal work",
            "received": "Deterrence of other firms from employing attorneys who worked on Trump cases"
        },
        "tags": ["law_firm", "executive_order", "coercion", "mueller", "jack_smith", "court_blocked", "unconstitutional"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Law firms sue Trump over executive orders targeting them",
                "url": "https://www.npr.org/2025/03/28/g-s1-56890/law-firms-sue-trump",
                "date": "2025-03-28",
                "outlet": "NPR",
                "type": "news"
            },
            {
                "title": "Trump executive order targeting Jenner & Block unconstitutional, judge rules",
                "url": "https://www.nbcnews.com/politics/justice-department/trump-executive-order-targeting-jenner-law-firm-unconstitutional-judge-rcna205230",
                "date": "2025-05-23",
                "outlet": "NBC News",
                "type": "news"
            },
            {
                "title": "WilmerHale executive order struck down by federal judge",
                "url": "https://www.washingtonpost.com/politics/2025/03/28/jenner-block-wilmer-hale-trump-law-firms-sue/",
                "date": "2025-03-28",
                "outlet": "Washington Post",
                "type": "news"
            }
        ]
    },
    {
        "id": "university-funding-columbia-2025-03",
        "date": "2025-03-07",
        "date_end": None,
        "title": "Columbia University capitulates after $400M funding cut — pays $220M+ to restore",
        "summary": "In March 2025, the Trump administration pulled more than $400 million in federal grants from Columbia University, explicitly linking the funding cut to Columbia's handling of pro-Palestinian protesters and campus demonstrations. The administration demanded Columbia change its disciplinary policies for protesters, place Middle Eastern, African, and South Asian studies programs under administrative control, and take other policy changes. Columbia largely capitulated to the demands — leading to the abrupt ouster of its interim president amid national backlash. The university agreed to pay the administration more than $220 million to restore federal funding. Critics called it the most consequential capitulation of any major American university to presidential pressure.",
        "categories": ["coercion_threat", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "Columbia University",
            "type": "organization",
            "country": "US",
            "description": "Ivy League university in New York City; $400M in federal grants pulled; capitulated to demands over pro-Palestinian protest policies"
        },
        "beneficiary": ["trump_personally", "republican_party"],
        "actors": ["Donald Trump", "Linda McMahon (Education Dept.)", "Department of Education"],
        "amount_usd": 400000000,
        "amount_note": "$400M+ in grants pulled; Columbia agreed to pay $220M+ to restore. Net federal leverage: hundreds of millions.",
        "financial_connection": {
            "exists": False,
            "description": "No direct Trump financial benefit. Political leverage: forcing policy changes at elite universities."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": "Change protest discipline policies; restructure Middle East studies; pay $220M+",
            "received": "Restoration of federal funding"
        },
        "tags": ["university", "federal_funding", "coercion", "dei", "columbia", "protest_policy"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Columbia University makes deal with Trump administration, agrees to pay more than $220 million to restore federal funding",
                "url": "https://www.pbs.org/newshour/politics/columbia-university-makes-deal-with-trump-administration-agrees-to-pay-more-than-220-million-to-restore-federal-funding",
                "date": "2025-04-21",
                "outlet": "PBS NewsHour",
                "type": "news"
            }
        ]
    },
    {
        "id": "university-funding-harvard-2025-04",
        "date": "2025-04-03",
        "date_end": None,
        "title": "Trump freezes $2.2B Harvard funding over DEI demands — Harvard refuses",
        "summary": "In April 2025, three federal agencies announced a review of approximately $8 billion in multi-year grants to Harvard University. After Harvard received a formal written list of demands — eliminate all DEI programs, ban masks at protests, derecognize pro-Palestinian student groups, audit academic departments for 'viewpoint diversity,' expel students involved in a 2023 protest altercation, and reform international student admissions to screen for those 'supportive of terrorism and antisemitism' — $2.2 billion in grants were immediately frozen after Harvard rejected the demands. Harvard was the only major American university to publicly refuse to comply. As of March 2026, nearly $9 billion in funding remains at risk and the legal battle is ongoing. The administration also threatened to revoke Harvard's tax-exempt status and threatened to bar international students from enrolling.",
        "categories": ["coercion_threat", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "Harvard University",
            "type": "organization",
            "country": "US",
            "description": "Oldest US university; $8B+ in federal grants at risk; refused Trump's DEI and protest policy demands; only major university to publicly resist"
        },
        "beneficiary": ["trump_personally", "republican_party"],
        "actors": ["Donald Trump", "Department of Education", "HHS", "NSF"],
        "amount_usd": 2200000000,
        "amount_note": "$2.2B immediately frozen; up to $9B total at risk across multiple agencies",
        "financial_connection": {
            "exists": False,
            "description": "No direct Trump financial benefit. Political pressure campaign against elite liberal university."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": "Demands: eliminate DEI, restructure admissions, expel students, audit departments",
            "received": "Restoration of federal funding — Harvard has refused"
        },
        "tags": ["university", "federal_funding", "coercion", "dei", "harvard", "protest_policy", "refused_to_comply"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Harvard's $2.3bn gamble: what Trump demanded, how the university resisted",
                "url": "https://www.aljazeera.com/news/2025/4/15/harvards-2-3bn-gamble-what-trump-demanded-how-the-university-resisted",
                "date": "2025-04-15",
                "outlet": "Al Jazeera",
                "type": "news"
            },
            {
                "title": "Trump administration freezes $2.2 billion in Harvard grants",
                "url": "https://www.cnbc.com/2025/04/14/trump-harvard-deal-funding-billion-dei.html",
                "date": "2025-04-14",
                "outlet": "CNBC",
                "type": "news"
            },
            {
                "title": "What Harvard demanded Trump — the full list of federal demands",
                "url": "https://www.thecrimson.com/article/2025/4/4/harvard-federal-funding-demands/",
                "date": "2025-04-04",
                "outlet": "Harvard Crimson",
                "type": "news"
            }
        ]
    },
    {
        "id": "university-funding-other-2025-04",
        "date": "2025-03-19",
        "date_end": None,
        "title": "Federal funding frozen at Penn ($175M), Princeton ($210M), Brown ($510M), Cornell ($1B+), Northwestern ($790M)",
        "summary": "In March and April 2025, the Trump administration froze federal funding at multiple major universities as leverage to force policy changes on DEI programs, protest discipline, and antisemitism policies. University of Pennsylvania: $175M frozen (March 19) — linked to its past policy permitting a transgender swimmer to compete on the women's team. Princeton: $210M frozen (April 1). Brown: $510M frozen (April 3). Cornell: over $1B frozen (April 8). Northwestern: $790M frozen (April 8) — Northwestern ultimately settled, paying the Trump administration $75 million. University of Pennsylvania rejected a subsequent 'higher education compact' from the administration (October 2025) that would have restored funding priority in exchange for eliminating DEI and limiting foreign student enrollment.",
        "categories": ["coercion_threat", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "University of Pennsylvania / Princeton / Brown / Cornell / Northwestern",
            "type": "organization",
            "country": "US",
            "description": "Five major research universities had federal funding frozen as leverage for DEI and protest policy changes; Northwestern paid $75M to settle"
        },
        "beneficiary": ["trump_personally", "republican_party"],
        "actors": ["Donald Trump", "Department of Education", "HHS"],
        "amount_usd": 2685000000,
        "amount_note": "Approximate total frozen: Penn $175M + Princeton $210M + Brown $510M + Cornell $1B + Northwestern $790M = ~$2.7B. Northwestern settled for $75M.",
        "financial_connection": {
            "exists": False,
            "description": "No direct Trump financial benefit. Political pressure against universities seen as liberal institutions."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": "DEI elimination; protest discipline reform; policy compliance",
            "received": "Restoration of federal funding"
        },
        "tags": ["university", "federal_funding", "coercion", "dei", "trans_athlete", "protest_policy"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "What to know about Trump's funding threats to colleges",
                "url": "https://www.insidehighered.com/news/government/politics-elections/2025/04/18/what-know-about-trumps-funding-threats-colleges",
                "date": "2025-04-18",
                "outlet": "Inside Higher Ed",
                "type": "news"
            },
            {
                "title": "Penn rejects Trump's higher education compact",
                "url": "https://www.highereddive.com/news/penn-rejects-trumps-higher-education-compact/803078/",
                "date": "2025-10-15",
                "outlet": "Higher Ed Dive",
                "type": "news"
            }
        ]
    },
    {
        "id": "media-abc-disney-settlement-2025-01",
        "date": "2024-12-16",
        "date_end": "2025-01-10",
        "title": "ABC/Disney pays $15M to Trump library to settle Stephanopoulos defamation suit",
        "summary": "In December 2024 (finalized January 2025), ABC and Disney settled a defamation lawsuit brought by Trump over anchor George Stephanopoulos's statements that Trump had been found 'liable for rape' in the E. Jean Carroll case (the jury found him liable for sexual abuse, not rape, though the judge later said the finding was consistent with rape). ABC/Disney paid $15 million to Trump's presidential library foundation and issued a public apology. Legal observers noted the settlement was influenced by the implicit threat of FCC regulatory action against ABC's broadcast licenses — FCC Chairman Brendan Carr, a Trump appointee, simultaneously held life-or-death power over ABC's affiliate stations. The settlement came before Trump's inauguration but was widely seen as shaped by the incoming administration's regulatory power.",
        "categories": ["coercion_threat", "business_payment"],
        "status": "confirmed",
        "counterparty": {
            "name": "ABC / Disney",
            "type": "organization",
            "country": "US",
            "description": "ABC News and parent company Disney; Stephanopoulos lawsuit settled; $15M to Trump presidential library; implicit FCC leverage"
        },
        "beneficiary": ["trump_personally", "trump_org"],
        "actors": ["Donald Trump", "FCC Chairman Brendan Carr"],
        "amount_usd": 15000000,
        "amount_note": "$15M to Trump presidential library foundation; public apology issued",
        "financial_connection": {
            "exists": True,
            "description": "$15M goes directly to Trump presidential library — a Trump-controlled entity. Settlement enabled by implicit FCC regulatory threat over ABC broadcast licenses."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "$15M to Trump library; public apology; coverage chilling effect",
            "received": "Settlement of lawsuit; relief from implicit FCC threat to ABC broadcast licenses"
        },
        "tags": ["media", "fcc", "lawsuit", "settlement", "coercion", "library", "abc", "disney", "stephanopoulos"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "ABC agrees to pay $15 million to Trump's presidential library to settle defamation lawsuit",
                "url": "https://www.pbs.org/newshour/politics/abc-agrees-to-pay-15-million-to-trumps-presidential-library-to-settle-defamation-lawsuit",
                "date": "2024-12-16",
                "outlet": "PBS NewsHour",
                "type": "news"
            },
            {
                "title": "ABC settles with Trump for $15 million — now he wants to sue other news outlets",
                "url": "https://www.npr.org/2024/12/16/nx-s1-5230274/abc-settles-with-trump-for-15-million-now-he-wants-to-sue-other-news-outlets",
                "date": "2024-12-16",
                "outlet": "NPR",
                "type": "news"
            }
        ]
    },
    {
        "id": "media-cbs-paramount-settlement-2025-07",
        "date": "2025-07-01",
        "date_end": "2025-07-24",
        "title": "Paramount/CBS pays $16M to Trump library — FCC merger approval granted 23 days later",
        "summary": "On July 1, 2025, Paramount Global (parent of CBS) settled a lawsuit Trump had brought over a CBS '60 Minutes' interview with Kamala Harris, in which CBS edited Harris's answer about Gaza. Trump alleged the editing was politically manipulative. Paramount paid $16 million to Trump's presidential library foundation. Critically, Paramount simultaneously needed FCC approval to complete its $8 billion merger with Skydance Media. FCC Chairman Brendan Carr (a Trump appointee) had delayed the merger review. The Skydance deal was approved on July 24, 2025 — 23 days after the settlement. Senators described the settlement as potentially 'an illegal bribe' in exchange for merger clearance. In a reported side deal, Skydance also agreed to give Trump $20 million in advertising and public service announcements, bringing the total value of the deal to at least $36 million. CBS newsroom staff reported significant internal turmoil over the settlement's implications for editorial independence.",
        "categories": ["coercion_threat", "business_payment"],
        "status": "confirmed",
        "counterparty": {
            "name": "CBS / Paramount Global / Skydance",
            "type": "organization",
            "country": "US",
            "description": "CBS parent Paramount needed FCC approval for Skydance merger; settled 60 Minutes lawsuit for $16M to Trump library; merger approved 23 days later"
        },
        "beneficiary": ["trump_personally", "trump_org"],
        "actors": ["Donald Trump", "FCC Chairman Brendan Carr", "Paramount Global", "Skydance Media"],
        "amount_usd": 36000000,
        "amount_note": "$16M to Trump presidential library + $20M in advertising/PSAs from Skydance = $36M total; FCC merger approval granted 23 days after settlement",
        "financial_connection": {
            "exists": True,
            "description": "$16M flows directly to Trump presidential library. Skydance agreed to $20M in ads/PSAs for Trump. FCC merger approval was the leverage: Paramount's $8B merger required FCC sign-off while Trump controlled the FCC."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "$16M to Trump library; $20M in Skydance advertising; retraction of editorial stance",
            "received": "FCC approval of Paramount-Skydance merger (approved July 24, 23 days after settlement)"
        },
        "tags": ["media", "fcc", "lawsuit", "settlement", "coercion", "library", "cbs", "paramount", "merger", "60_minutes"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "CBS and Trump settle lawsuit over 60 Minutes Kamala Harris interview",
                "url": "https://www.cnn.com/2025/07/02/media/cbs-trump-60-minutes-paramount-settlement",
                "date": "2025-07-02",
                "outlet": "CNN",
                "type": "news"
            },
            {
                "title": "Trump lawsuit against Paramount — CBS 60 Minutes, Kamala Harris",
                "url": "https://www.npr.org/2025/07/02/nx-s1-5290171/trump-lawsuit-paramount-cbs-60-minutes-kamala-harris",
                "date": "2025-07-02",
                "outlet": "NPR",
                "type": "news"
            },
            {
                "title": "Paramount's Trump lawsuit settlement — curtain call for the First Amendment",
                "url": "https://knightcolumbia.org/blog/paramounts-trump-lawsuit-settlement-curtain-call-for-the-first-amendment",
                "date": "2025-07-10",
                "outlet": "Knight First Amendment Institute",
                "type": "analysis"
            }
        ]
    },
    {
        "id": "media-fcc-broadcast-license-threats-2025",
        "date": "2025-09-19",
        "date_end": "2026-03-14",
        "title": "FCC threatens to revoke broadcast licenses of ABC, NBC, CBS over news coverage",
        "summary": "FCC Chairman Brendan Carr, a Trump appointee, repeatedly threatened to revoke or not renew broadcast licenses of major television networks — ABC, NBC, and CBS — over their news coverage. On September 19, 2025, Trump called ABC and NBC 'two of the worst and most biased networks in history' and suggested license revocation would 'be up to' FCC Chairman Carr. Carr had previously (in a 2025 incident) pressured ABC into pulling Jimmy Kimmel's show from one night of programming after Kimmel made a comment about the assassination of Charlie Kirk. In March 2026, Carr threatened broadcasters' local station licenses over their coverage of the US-Iran war. Legal experts noted that revoking the licenses of major broadcast networks is procedurally nearly impossible and would take years — but the threat created a documented chilling effect on coverage and editorial decisions.",
        "categories": ["coercion_threat", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "ABC / NBC / CBS broadcast networks",
            "type": "organization",
            "country": "US",
            "description": "The three major US broadcast networks targeted with FCC license revocation threats over news coverage Trump disliked"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "FCC Chairman Brendan Carr", "FCC"],
        "amount_usd": None,
        "amount_note": "No direct financial transaction; economic value is the chilling effect on media coverage of Trump",
        "financial_connection": {
            "exists": False,
            "description": "No direct financial benefit to Trump. Control over media narrative through regulatory intimidation."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Threat of license revocation over unfavorable coverage",
            "received": "Chilling effect on coverage; documented self-censorship (Kimmel show pulled, other decisions)"
        },
        "tags": ["media", "fcc", "broadcast_license", "coercion", "press_freedom", "iran_war", "chilling_effect"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump threatening broadcast station licenses — explained",
                "url": "https://www.cnbc.com/2025/09/19/trump-threatening-broadcast-station-licenses-explained.html",
                "date": "2025-09-19",
                "outlet": "CNBC",
                "type": "news"
            },
            {
                "title": "FCC threatens TV broadcast licenses over Iran war news coverage",
                "url": "https://fortune.com/2026/03/14/fcc-brendan-carr-tv-broadcast-licenses-news-coverage-us-war-iran-trump/",
                "date": "2026-03-14",
                "outlet": "Fortune",
                "type": "news"
            },
            {
                "title": "FCC Brendan Carr threat to news networks — broadcast license",
                "url": "https://www.cbsnews.com/news/fcc-brendan-carr-threat-news-networks-broadcast-license/",
                "date": "2026-03-14",
                "outlet": "CBS News",
                "type": "news"
            }
        ]
    },
    {
        "id": "trump-nyt-lawsuit-2025-09",
        "date": "2025-09-16",
        "date_end": None,
        "title": "Trump files $15B defamation lawsuit against New York Times",
        "summary": "In September 2025, Trump filed a $15 billion defamation and libel lawsuit against the New York Times over a book and several articles. A federal judge in Tampa dismissed the original complaint as 'decidedly improper and impermissible' but allowed refiling within 28 days. Trump refiled in October 2025. The lawsuit is widely regarded by First Amendment lawyers as meritless and legally frivolous under the actual malice standard established in New York Times v. Sullivan — but the cost of defending the lawsuit is itself significant. Critics including press freedom organizations called the suit an attempt to intimidate the Times and chill its reporting on Trump. Trump has also publicly called for the Supreme Court to revisit and overturn the New York Times v. Sullivan precedent.",
        "categories": ["coercion_threat", "retaliation_targeting"],
        "status": "confirmed",
        "counterparty": {
            "name": "New York Times",
            "type": "organization",
            "country": "US",
            "description": "Major US newspaper; sued for $15B by Trump; dismissed once, refiled; Trump has called for overturning NYT v. Sullivan press protection precedent"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump"],
        "amount_usd": 15000000000,
        "amount_note": "$15B claimed in lawsuit; considered legally frivolous by First Amendment lawyers; actual value is chilling effect on coverage",
        "financial_connection": {
            "exists": False,
            "description": "No direct financial benefit expected. Lawsuit is widely seen as harassment and intimidation of press."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Existential legal threat requiring significant defense resources",
            "received": "Potential chilling effect on Times' reporting on Trump"
        },
        "tags": ["media", "lawsuit", "coercion", "press_freedom", "nyt", "defamation"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump files $15 billion lawsuit against the New York Times",
                "url": "https://www.npr.org/2025/09/16/nx-s1-5543030/donald-trump-nytimes-lawsuit",
                "date": "2025-09-16",
                "outlet": "NPR",
                "type": "news"
            }
        ]
    },
    {
        "id": "intel-chips-act-coercion-2025-08",
        "date": "2025-08-01",
        "date_end": "2025-08-22",
        "title": "Trump withholds CHIPS Act funds — forces Intel to give US government 10% equity stake",
        "summary": "Intel had been awarded $8.9 billion in CHIPS Act grants by the Biden administration to fund domestic semiconductor manufacturing. Trump withheld the congressionally approved funds and, two weeks before Intel agreed to the deal, publicly called for Intel CEO Lip-Bu Tan to resign, alleging problematic ties to China. Intel agreed to give the US government a 10% equity stake in the company in exchange for release of the $8.9 billion in CHIPS Act funds (August 2025). Commerce Secretary Lutnick confirmed the equity stake was part of the deal. The administration indicated it may seek similar equity arrangements from other CHIPS Act recipients. Critics noted this was an unprecedented use of congressionally approved funding as leverage to extract equity from private corporations.",
        "categories": ["coercion_threat", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "Intel Corporation",
            "type": "organization",
            "country": "US",
            "description": "US semiconductor company; had $8.9B CHIPS Act funding withheld; forced to give US government 10% equity stake to receive congressionally approved funds"
        },
        "beneficiary": ["us_government"],
        "actors": ["Donald Trump", "Howard Lutnick (Commerce Secretary)", "Department of Commerce"],
        "amount_usd": 8900000000,
        "amount_note": "$8.9B in CHIPS Act funds released in exchange for 10% government equity stake in Intel",
        "financial_connection": {
            "exists": True,
            "description": "US government acquired 10% equity stake in Intel (a private corporation) as condition for releasing congressionally approved CHIPS Act funds. Unprecedented use of funding leverage to extract corporate equity."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": "10% equity stake in Intel to US government",
            "received": "Release of $8.9B in CHIPS Act funds that had been withheld"
        },
        "tags": ["chips_act", "coercion", "intel", "semiconductor", "equity_stake", "corporate_coercion"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump says US government will take stake in Intel",
                "url": "https://www.npr.org/2025/08/22/nx-s1-5509673/trump-says-us-government-will-take-stake-intel",
                "date": "2025-08-22",
                "outlet": "NPR",
                "type": "news"
            },
            {
                "title": "Lutnick: Intel equity stake part of CHIPS Act deal",
                "url": "https://www.cnbc.com/2025/08/19/lutnick-intel-stock-chips-trump.html",
                "date": "2025-08-19",
                "outlet": "CNBC",
                "type": "news"
            }
        ]
    }
]

# Append new incidents
incidents.extend(new_incidents)
data["incidents"] = incidents
data["last_updated"] = "2026-03-28"

with open(DATA, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Total incidents: {len(incidents)}")
print("Added incidents:")
for inc in new_incidents:
    print(f"  {inc['id']}")
    print(f"    {inc['title'][:80]}")
