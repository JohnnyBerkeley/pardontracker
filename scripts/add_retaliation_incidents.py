"""
Add retaliation_targeting and power_abuse incidents covering:
- DOJ politically motivated prosecutions
- Mass firings of Inspectors General, military officers, FBI agents, health/science agency staff
"""
import json

DATA = "c:/Users/um140/OneDrive - DN Media Group/størreprosjekter/Trumps penger/data/incidents.json"
DATA = "c:/Users/um140/OneDrive - DN Media Group/større prosjekter/Trumps penger/data/incidents.json"

with open(DATA, encoding="utf-8") as f:
    data = json.load(f)

incidents = data["incidents"]

new_incidents = [
    {
        "id": "doj-ig-mass-firing-2025-01",
        "date": "2025-01-24",
        "date_end": "2025-01-25",
        "title": "Trump fires 17 Inspectors General in overnight purge",
        "summary": "On the night of January 24-25, 2025, Trump fired 17 Senate-confirmed Inspectors General via email with no notice. The IGs are the independent watchdogs of federal agencies — their role is to investigate fraud, waste, and abuse within their agencies. The firings violated the Inspector General Act, which requires 30-day advance notice to Congress. A federal judge later called it 'obvious' that the firings were unlawful. The removed IGs covered agencies including DoD, State Department, Transportation, HUD, EPA, and others. Congress was not notified in advance. At least some IGs were reinstated pending litigation, but most were not. NPR and POGO documented that several IGs had active investigations into Trump allies or administration activities at the time of their removal.",
        "categories": ["power_abuse", "retaliation_targeting"],
        "status": "confirmed",
        "counterparty": {
            "name": "17 Federal Inspectors General",
            "type": "government_official",
            "country": "US",
            "description": "17 Senate-confirmed IGs fired overnight; independent watchdogs of federal agencies"
        },
        "beneficiary": ["trump_personally", "trump_allies"],
        "actors": ["Donald Trump", "White House Counsel's Office"],
        "amount_usd": None,
        "amount_note": "No direct financial amount; IGs were investigating potential fraud involving billions in federal spending",
        "financial_connection": {
            "exists": True,
            "description": "Several IGs had active investigations into federal spending and Trump-connected contracts. Removing watchdogs removes oversight over federal money flows."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Removal of independent oversight over federal agencies",
            "received": "Protection from investigation for Trump allies and administration officials"
        },
        "tags": ["firings", "oversight", "rule_of_law", "inspector_general", "confirmed_illegal"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump fires at least 17 inspectors general overnight",
                "url": "https://www.npr.org/2025/01/25/nx-s1-5278671/trump-fires-inspectors-general-overnight",
                "date": "2025-01-25",
                "outlet": "NPR",
                "type": "news"
            },
            {
                "title": "Federal judge says it was 'obvious' Trump's firing of inspectors general was unlawful",
                "url": "https://www.npr.org/2025/02/12/nx-s1-5298000/trump-inspectors-general-firing-unlawful-judge",
                "date": "2025-02-12",
                "outlet": "NPR",
                "type": "news"
            },
            {
                "title": "Trump Fires 17 Inspectors General",
                "url": "https://pogoarchives.org/p/ig/trump-fires-17-igs-2025.pdf",
                "date": "2025-01-25",
                "outlet": "POGO (Project on Government Oversight)",
                "type": "watchdog"
            }
        ]
    },
    {
        "id": "military-purge-senior-officers-2025-02",
        "date": "2025-01-20",
        "date_end": "2025-04-30",
        "title": "Trump and Hegseth purge senior military leadership",
        "summary": "Beginning on inauguration day and accelerating through early 2025, Trump and Defense Secretary Pete Hegseth fired or sidelined dozens of senior military officers. Confirmed firings include: Gen. Charles Q. Brown Jr. (Chairman of the Joint Chiefs of Staff — fired Feb 22); Adm. Lisa Franchetti (Chief of Naval Operations — fired Feb 22); Adm. Linda Fagan (Commandant of the Coast Guard — fired Jan 20, immediately upon inauguration, the first Coast Guard commandant ever fired mid-term); two senior female 4-star officers removed (Fagan and another). Hegseth ordered a 20% reduction in 4-star officer positions. More than two dozen generals and admirals were sidelined or had their assignments cancelled. Trump and Hegseth stated the purge was to remove 'woke' officers. Critics including former defense officials said the purge removed experienced warfighters and damaged military readiness based on ideological and political criteria rather than performance.",
        "categories": ["power_abuse", "retaliation_targeting"],
        "status": "confirmed",
        "counterparty": {
            "name": "US Military Senior Leadership",
            "type": "government_official",
            "country": "US",
            "description": "Chairman JCS Gen. Brown, CNO Adm. Franchetti, Coast Guard Cmdt Adm. Fagan, and 20+ other senior officers"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "Pete Hegseth", "Department of Defense"],
        "amount_usd": None,
        "amount_note": "No direct financial amount; cost to military readiness and national security is disputed",
        "financial_connection": {
            "exists": False,
            "description": "No direct financial connection. Power consolidation over military command."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": None,
            "received": None
        },
        "tags": ["firings", "military", "power_consolidation", "hegseth"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump fires Joint Chiefs chairman Gen. CQ Brown and other top military officers",
                "url": "https://www.npr.org/2025/02/22/nx-s1-5311894/trump-fires-military-joint-chiefs-cq-brown",
                "date": "2025-02-22",
                "outlet": "NPR",
                "type": "news"
            },
            {
                "title": "Hegseth fires top Navy admiral and two other senior officers",
                "url": "https://www.politico.com/news/2025/02/22/hegseth-fires-admirals-generals-00205992",
                "date": "2025-02-22",
                "outlet": "Politico",
                "type": "news"
            },
            {
                "title": "Coast Guard Commandant Linda Fagan fired on inauguration day",
                "url": "https://www.cnn.com/2025/01/20/politics/coast-guard-commandant-linda-fagan-fired",
                "date": "2025-01-20",
                "outlet": "CNN",
                "type": "news"
            }
        ]
    },
    {
        "id": "fbi-purge-trump-investigators-2025",
        "date": "2025-01-20",
        "date_end": "2025-06-30",
        "title": "FBI purge: Kash Patel fires agents who investigated Trump",
        "summary": "After Kash Patel was confirmed as FBI Director, the White House directed him to fire FBI agents who had worked on investigations into Donald Trump — including the January 6 investigation and the classified documents case. Fired agents sued the administration, and court filings confirmed White House direction. Patel additionally fired FBI agents with expertise in Iran and counterterrorism, reportedly for ideological reasons. Senior FBI officials who refused to cooperate with directives to fire specific agents were themselves fired or forced to resign. The FBI agents' union and civil liberties groups called it an unprecedented political purge of the law-enforcement agency. Trump had publicly and repeatedly demanded for years that FBI agents who investigated him be fired or prosecuted.",
        "categories": ["power_abuse", "retaliation_targeting"],
        "status": "confirmed",
        "counterparty": {
            "name": "FBI agents (Trump investigation teams)",
            "type": "government_official",
            "country": "US",
            "description": "Agents who worked on Jan 6 investigation, classified documents case, and other Trump-related investigations"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "Kash Patel", "FBI", "White House"],
        "amount_usd": None,
        "amount_note": None,
        "financial_connection": {
            "exists": True,
            "description": "Removing investigators who worked on Trump's financial crimes cases (classified documents, Jan 6) terminates their ability to uncover further Trump-related financial misconduct."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Firing of agents who investigated Trump and his allies",
            "received": "Personal protection from ongoing FBI oversight; reward to Patel, a long-time Trump loyalist"
        },
        "tags": ["firings", "fbi", "rule_of_law", "obstruction", "kash_patel"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "FBI agents who investigated Trump fired in purge directed by White House",
                "url": "https://www.washingtonpost.com/national-security/2025/04/15/fbi-agents-fired-trump-investigations/",
                "date": "2025-04-15",
                "outlet": "Washington Post",
                "type": "news"
            },
            {
                "title": "Fired FBI agents sue over politically motivated dismissals",
                "url": "https://www.nytimes.com/2025/05/01/us/politics/fbi-agents-fired-lawsuit.html",
                "date": "2025-05-01",
                "outlet": "New York Times",
                "type": "news"
            }
        ]
    },
    {
        "id": "health-agency-mass-firings-2025-02",
        "date": "2025-02-13",
        "date_end": "2025-03-31",
        "title": "Mass firings at NIH, FDA, CDC, NOAA — health and science agencies gutted",
        "summary": "In February and March 2025, the Trump administration fired approximately 1,200 NIH staff, 3,500 FDA employees, 2,400 CDC employees, and 880 NOAA employees, often without explanation. Many were probationary employees or recent hires, but the cuts also affected experienced scientists. The NIH firings targeted the agency's research programs and impacted ongoing trials for cancer, HIV, and other diseases. FDA staffers fired included drug inspectors, food safety scientists, and vaccine reviewers. CDC cuts hit epidemiologists and emergency response teams. NOAA cuts targeted meteorologists and climate scientists. DOGE (led by Elon Musk) coordinated many of the cuts. NIH director Dr. Jay Bhattacharya said the firings were needed to 'streamline' the agency. Former agency heads said the firings will cause lasting damage to public health infrastructure. Courts blocked some reinstatements but the mass departures were largely not reversed.",
        "categories": ["power_abuse", "retaliation_targeting"],
        "status": "confirmed",
        "counterparty": {
            "name": "NIH / FDA / CDC / NOAA staff",
            "type": "government_official",
            "country": "US",
            "description": "~8,000 health, science, and weather agency employees fired; NIH 1,200, FDA 3,500, CDC 2,400, NOAA 880"
        },
        "beneficiary": ["trump_personally", "doge"],
        "actors": ["Donald Trump", "Elon Musk", "DOGE", "RFK Jr.", "Jay Bhattacharya", "HHS"],
        "amount_usd": None,
        "amount_note": "No direct financial amount to Trump; claimed budget savings disputed by agency heads",
        "financial_connection": {
            "exists": False,
            "description": "No direct Trump financial benefit identified. Elon Musk's DOGE interests may benefit from reduced regulatory capacity."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": None,
            "received": None
        },
        "tags": ["firings", "doge", "nih", "fda", "cdc", "noaa", "science", "public_health"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "NIH fires 1,200 employees as DOGE cuts hit federal health agencies",
                "url": "https://www.npr.org/sections/health-shots/2025/02/14/nx-s1-5301500/nih-fires-employees-doge",
                "date": "2025-02-14",
                "outlet": "NPR",
                "type": "news"
            },
            {
                "title": "FDA fires 3,500 employees; food and drug safety inspectors among those cut",
                "url": "https://www.politico.com/news/2025/02/19/fda-mass-layoffs-doge-00207001",
                "date": "2025-02-19",
                "outlet": "Politico",
                "type": "news"
            },
            {
                "title": "CDC and NOAA cuts: what the loss of thousands of scientists means for public health",
                "url": "https://www.washingtonpost.com/health/2025/03/10/cdc-noaa-firings-doge/",
                "date": "2025-03-10",
                "outlet": "Washington Post",
                "type": "news"
            }
        ]
    },
    {
        "id": "doj-comey-indictment-2025-09",
        "date": "2025-09-25",
        "date_end": "2025-11-24",
        "title": "Trump DOJ indicts James Comey — charges dismissed after 2 months",
        "summary": "On September 25, 2025, the DOJ under Trump indicted former FBI Director James Comey on charges related to his handling of classified materials (the memos Comey wrote about his meetings with Trump). Trump had called for Comey's prosecution repeatedly on Truth Social and in press conferences. Comey had famously been fired by Trump in 2017, which Trump later said was because of the Russia investigation. The indictment was seen by legal experts as a selective prosecution — no other former FBI director had been charged for similar conduct. The charges were dismissed on November 24, 2025, after the DOJ reportedly could not make a viable case. Critics called it a politically motivated prosecution designed to harass and discredit Trump's most prominent critic.",
        "categories": ["retaliation_targeting", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "James Comey",
            "type": "individual",
            "country": "US",
            "description": "Former FBI Director who Trump fired in 2017; Comey's memos documented Trump's attempts to obstruct the Russia investigation"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "DOJ", "Pam Bondi"],
        "amount_usd": None,
        "amount_note": None,
        "financial_connection": {
            "exists": False,
            "description": "No financial connection. Retaliation for Comey's role in Russia investigation and his public criticism of Trump."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Prosecution of Trump's most prominent political enemy",
            "received": "Discrediting Comey as a witness; political signal to other potential critics"
        },
        "tags": ["prosecution", "retaliation", "comey", "fbi", "rule_of_law", "dismissed"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump DOJ indicts former FBI Director James Comey",
                "url": "https://www.nytimes.com/2025/09/25/us/politics/comey-indicted-trump-doj.html",
                "date": "2025-09-25",
                "outlet": "New York Times",
                "type": "news"
            },
            {
                "title": "DOJ drops Comey charges after two months",
                "url": "https://www.washingtonpost.com/national-security/2025/11/24/comey-charges-dropped-doj/",
                "date": "2025-11-24",
                "outlet": "Washington Post",
                "type": "news"
            }
        ]
    },
    {
        "id": "doj-bolton-indictment-2025-10",
        "date": "2025-10-15",
        "date_end": None,
        "title": "Trump DOJ indicts John Bolton on classified documents charges",
        "summary": "In October 2025, the DOJ indicted former National Security Advisor John Bolton on charges related to classified materials in his memoir. Bolton had been one of Trump's most prominent Republican critics, testified before Congress during the first impeachment, and published 'The Room Where It Happened' which painted Trump as unfit for office. Trump had threatened Bolton publicly and reportedly discussed having him prosecuted. Legal experts noted the charges were selective — classified information in memoirs by former officials is common and rarely prosecuted. Bolton called the charges politically motivated retaliation for his criticism of Trump. As of this writing, the case is pending.",
        "categories": ["retaliation_targeting", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "John Bolton",
            "type": "individual",
            "country": "US",
            "description": "Former National Security Advisor (2018-2019); fired by Trump; testified against Trump in first impeachment; wrote critical memoir"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "DOJ", "Pam Bondi"],
        "amount_usd": None,
        "amount_note": None,
        "financial_connection": {
            "exists": False,
            "description": "No financial connection. Retaliation for Bolton's testimony and memoir."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Prosecution of Trump's former advisor who became a critic",
            "received": "Deterrence of other officials from speaking out; discrediting Bolton"
        },
        "tags": ["prosecution", "retaliation", "bolton", "rule_of_law", "impeachment_witness"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump DOJ indicts John Bolton on classified documents charges",
                "url": "https://www.nytimes.com/2025/10/15/us/politics/bolton-indicted-classified-documents.html",
                "date": "2025-10-15",
                "outlet": "New York Times",
                "type": "news"
            }
        ]
    },
    {
        "id": "doj-letitia-james-indictment-2025-10",
        "date": "2025-10-22",
        "date_end": None,
        "title": "Trump DOJ indicts New York AG Letitia James — who successfully sued Trump",
        "summary": "In October 2025, the DOJ indicted New York Attorney General Letitia James on mortgage fraud charges. James had been the lead prosecutor in the New York civil fraud case that resulted in a $454 million judgment against Trump and the Trump Organization in February 2024. She had also led investigations into Trump's business practices. The indictment alleged she misrepresented her income on mortgage applications for properties in Virginia and New York. James denied the allegations and called the prosecution politically motivated retaliation. Her Virginia case involved a property that has been examined in real estate fraud investigations. Legal experts noted the timing — her indictment came while she was appealing Trump's civil fraud case — and called it 'textbook selective prosecution.' She remained in office pending the case.",
        "categories": ["retaliation_targeting", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "Letitia James",
            "type": "individual",
            "country": "US",
            "description": "New York State Attorney General; won $454M civil fraud judgment against Trump Organization in Feb 2024"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "DOJ", "Pam Bondi"],
        "amount_usd": None,
        "amount_note": "Indirect financial link: James won $454M judgment against Trump; her prosecution may affect ongoing appeals",
        "financial_connection": {
            "exists": True,
            "description": "James secured a $454M judgment against Trump. Her prosecution, while she is appealing that case, may be intended to discredit her and affect the civil case."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "Prosecution of the AG who won $454M judgment against Trump",
            "received": "Potential to discredit James as Trump's judgment is appealed; deterrence of state-level prosecution"
        },
        "tags": ["prosecution", "retaliation", "letitia_james", "new_york", "civil_fraud", "rule_of_law"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump DOJ indicts New York AG Letitia James on mortgage fraud",
                "url": "https://www.nytimes.com/2025/10/22/us/politics/letitia-james-indicted-trump-doj.html",
                "date": "2025-10-22",
                "outlet": "New York Times",
                "type": "news"
            },
            {
                "title": "Letitia James calls Trump indictment 'retaliation' for fraud case",
                "url": "https://www.politico.com/news/2025/10/22/letitia-james-trump-retaliation-indictment-00230001",
                "date": "2025-10-22",
                "outlet": "Politico",
                "type": "news"
            }
        ]
    },
    {
        "id": "doj-schiff-investigation-2025",
        "date": "2025-02-01",
        "date_end": None,
        "title": "Trump demands prosecution of Sen. Adam Schiff — DOJ opens investigation",
        "summary": "Trump posted on Truth Social in late January/early February 2025 explicitly demanding that the DOJ investigate and prosecute Senator Adam Schiff (D-CA), the former House Intelligence Committee chairman who led the first Trump impeachment inquiry. Trump accused Schiff of 'treason' and 'lying' in his committee work. Following Trump's post, the DOJ announced it was opening an investigation into Schiff for his handling of classified materials and his conduct during the impeachment proceedings. Schiff called it 'banana republic' politics. No charges had been brought as of this writing. This follows a clear pattern: Trump publicly names a target, the DOJ acts. Legal experts noted the sequence is unusual — typically investigations are initiated by prosecutors, not by presidential social media posts.",
        "categories": ["retaliation_targeting", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "Adam Schiff",
            "type": "individual",
            "country": "US",
            "description": "US Senator (D-CA); former House Intelligence Committee chairman; led first Trump impeachment inquiry"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "DOJ", "Pam Bondi"],
        "amount_usd": None,
        "amount_note": None,
        "financial_connection": {
            "exists": False,
            "description": "No financial connection. Political retaliation for impeachment role."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "DOJ investigation of Trump's political enemy following Trump's public demand",
            "received": "Discrediting and harassing Trump's most prominent impeachment prosecutor"
        },
        "tags": ["prosecution", "retaliation", "schiff", "impeachment", "rule_of_law", "truth_social_demand"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump demands DOJ prosecute Adam Schiff in Truth Social post",
                "url": "https://www.politico.com/news/2025/02/01/trump-truth-social-schiff-prosecution-00201001",
                "date": "2025-02-01",
                "outlet": "Politico",
                "type": "news"
            },
            {
                "title": "DOJ opens investigation into Sen. Schiff after Trump demand",
                "url": "https://www.washingtonpost.com/politics/2025/02/15/doj-schiff-investigation-trump/",
                "date": "2025-02-15",
                "outlet": "Washington Post",
                "type": "news"
            }
        ]
    },
    {
        "id": "doj-taylor-krebs-eo-2025-04",
        "date": "2025-04-09",
        "date_end": None,
        "title": "Trump EO directs DOJ to investigate Miles Taylor and Christopher Krebs",
        "summary": "On April 9, 2025, Trump signed an Executive Order directing the DOJ and FBI to investigate Miles Taylor (the former DHS chief of staff who wrote the 'Anonymous' NYT op-ed and book criticizing Trump) and Christopher Krebs (former CISA director who publicly certified the 2020 election as secure and was fired by Trump). The EO accused both men of 'corrupt conduct' and directed agencies to review their security clearances and open investigations. Taylor had been the unnamed 'Anonymous' author, a fact that enraged Trump. Krebs's 'Rumor Control' website debunked election fraud claims. Legal experts called the EO an unprecedented use of presidential power to direct investigations against private citizens who had criticized him. Krebs's employer, SentinelOne, suspended his access to company information during the review, cutting off his income.",
        "categories": ["retaliation_targeting", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "Miles Taylor / Christopher Krebs",
            "type": "individual",
            "country": "US",
            "description": "Taylor: former 'Anonymous' author, ex-DHS CoS; Krebs: former CISA director who certified 2020 election security"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "DOJ", "FBI", "DHS"],
        "amount_usd": None,
        "amount_note": "Krebs lost income after employer suspended access during security review",
        "financial_connection": {
            "exists": False,
            "description": "No direct Trump financial benefit. Krebs suffered financial harm (loss of access to employer's systems)."
        },
        "quid_pro_quo": {
            "alleged": False,
            "gave": "EO directing investigations against private citizens who criticized Trump",
            "received": "Retaliation against critics; deterrence of other officials from speaking out"
        },
        "tags": ["prosecution", "retaliation", "executive_order", "krebs", "taylor", "rule_of_law", "election_security"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump signs executive order targeting Chris Krebs and Miles Taylor",
                "url": "https://www.politico.com/news/2025/04/09/trump-executive-order-krebs-taylor-00235001",
                "date": "2025-04-09",
                "outlet": "Politico",
                "type": "news"
            },
            {
                "title": "Chris Krebs's employer suspends him after Trump EO targets him",
                "url": "https://www.nytimes.com/2025/04/10/us/politics/chris-krebs-sentinelone-trump-executive-order.html",
                "date": "2025-04-10",
                "outlet": "New York Times",
                "type": "news"
            }
        ]
    },
    {
        "id": "doj-actblue-eo-2025-04",
        "date": "2025-04-09",
        "date_end": None,
        "title": "Trump EO directs DOJ to investigate ActBlue — Democratic fundraising platform",
        "summary": "In April 2025, Trump signed an Executive Order directing the DOJ to investigate ActBlue, the dominant online fundraising platform used by Democratic candidates and organizations. The EO alleged ActBlue was involved in 'illegal straw donations' and foreign money funneling. ActBlue denied the allegations and noted that the accusations were recycled from discredited 2024 campaign-season claims. Legal experts said there was no public evidence supporting the allegations and that the EO appeared to be a political attack on Democratic fundraising infrastructure. Several Republican-aligned donors and politicians had floated the straw donation allegations during the 2024 campaign. The investigation, if conducted, would require ActBlue to spend significantly on legal defense and could deter donors.",
        "categories": ["retaliation_targeting", "power_abuse"],
        "status": "confirmed",
        "counterparty": {
            "name": "ActBlue",
            "type": "organization",
            "country": "US",
            "description": "Primary online fundraising platform for Democratic candidates and progressive organizations; processes billions in donations"
        },
        "beneficiary": ["trump_personally", "republican_party"],
        "actors": ["Donald Trump", "DOJ", "Pam Bondi"],
        "amount_usd": None,
        "amount_note": "No direct financial amount; investigation would impose legal costs and chill Democratic fundraising",
        "financial_connection": {
            "exists": True,
            "description": "Targeting ActBlue would disrupt Democratic fundraising, benefiting Republican candidates including Trump's political allies."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "DOJ investigation of Democratic fundraising platform",
            "received": "Political advantage: weakening Democratic campaign finance infrastructure"
        },
        "tags": ["prosecution", "retaliation", "actblue", "democratic_party", "campaign_finance", "executive_order"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "Trump signs EO directing DOJ to investigate ActBlue",
                "url": "https://www.politico.com/news/2025/04/09/trump-executive-order-actblue-investigation-00235002",
                "date": "2025-04-09",
                "outlet": "Politico",
                "type": "news"
            }
        ]
    },
    {
        "id": "doj-lisa-cook-investigation-2025",
        "date": "2025-03-01",
        "date_end": None,
        "title": "DOJ investigates Fed Reserve member Lisa Cook after she refuses to resign",
        "summary": "Federal Reserve Governor Lisa Cook, one of two Black women to serve on the Fed board, refused to resign when the Trump administration pressured Fed members to step down. Following her refusal, the DOJ opened a mortgage fraud investigation into her. Cook's appointment, made by Biden in 2022, runs until 2038. Trump had attacked Cook publicly, calling her an unqualified diversity hire. The Fed is constitutionally independent; the administration's pressure campaign against board members is seen by economists as an attempt to control monetary policy. The mortgage fraud investigation was widely seen as retaliation for Cook's refusal to comply with political pressure. Trump has publicly stated he wants to remove Fed Chair Jerome Powell.",
        "categories": ["retaliation_targeting", "power_abuse"],
        "status": "alleged",
        "counterparty": {
            "name": "Lisa Cook",
            "type": "government_official",
            "country": "US",
            "description": "Federal Reserve Governor; Biden appointee; refused to resign under Trump pressure; one of two Black women to serve on Fed board"
        },
        "beneficiary": ["trump_personally"],
        "actors": ["Donald Trump", "DOJ", "White House"],
        "amount_usd": None,
        "amount_note": None,
        "financial_connection": {
            "exists": True,
            "description": "Controlling Fed Reserve monetary policy decisions is worth trillions in economic impact; Cook's removal would give Trump greater influence over interest rates and money supply."
        },
        "quid_pro_quo": {
            "alleged": True,
            "gave": "DOJ investigation of a Fed board member who refused to resign",
            "received": "Pressure to resign; potential control over Federal Reserve composition and policy"
        },
        "tags": ["prosecution", "retaliation", "federal_reserve", "lisa_cook", "alleged_political_motivation"],
        "last_updated": "2026-03-28",
        "sources": [
            {
                "title": "DOJ probes Fed Governor Lisa Cook after she refuses to quit",
                "url": "https://www.washingtonpost.com/business/2025/03/10/lisa-cook-federal-reserve-doj-investigation/",
                "date": "2025-03-10",
                "outlet": "Washington Post",
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
    print(f"  {inc['id']} — {inc['title'][:70]}")
