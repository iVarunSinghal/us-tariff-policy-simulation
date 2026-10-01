import pandas as pd

events = [
    {
        "event_name": "Section 232 Steel Tariff",
        "legal_authority": "Section 232 Trade Expansion Act",
        "country_code": "ALL",
        "hs_chapters": "72,73",
        "additional_rate": 0.25,
        "effective_date": "2018-03-23",
        "end_date": None,
        "note": "25% on raw steel imports"
    },
    {
        "event_name": "Section 301 List 1",
        "legal_authority": "Section 301 Trade Act",
        "country_code": "156",
        "hs_chapters": "84,85,90",
        "additional_rate": 0.25,
        "effective_date": "2018-07-06",
        "end_date": None,
        "note": "Industrial machinery, electronics components"
    },
    {
        "event_name": "Section 301 List 2",
        "legal_authority": "Section 301 Trade Act",
        "country_code": "156",
        "hs_chapters": "84,85,87",
        "additional_rate": 0.25,
        "effective_date": "2018-08-23",
        "end_date": None,
        "note": "Semiconductors, plastics, machinery"
    },
    {
        "event_name": "Section 301 List 3 (initial)",
        "legal_authority": "Section 301 Trade Act",
        "country_code": "156",
        "hs_chapters": "84,85,94,62",
        "additional_rate": 0.10,
        "effective_date": "2018-09-24",
        "end_date": "2019-05-09",
        "note": "Started at 10%, escalated to 25% in May 2019"
    },
    {
        "event_name": "Section 301 List 3 (escalated)",
        "legal_authority": "Section 301 Trade Act",
        "country_code": "156",
        "hs_chapters": "84,85,94,62",
        "additional_rate": 0.25,
        "effective_date": "2019-05-10",
        "end_date": None,
        "note": "5,745 HTS lines; broad coverage"
    },
    {
        "event_name": "Section 301 List 4A",
        "legal_authority": "Section 301 Trade Act",
        "country_code": "156",
        "hs_chapters": "85,61,62,64",
        "additional_rate": 0.075,
        "effective_date": "2019-09-01",
        "end_date": None,
        "note": "Phase 1 deal reduced from 15% to 7.5% in Feb 2020"
    },
    {
        "event_name": "Biden EV Tariff Hike",
        "legal_authority": "Section 301 (modified)",
        "country_code": "156",
        "hs_chapters": "87",
        "additional_rate": 1.00,
        "effective_date": "2024-08-01",
        "end_date": None,
        "note": "Electric vehicles from China: 100% tariff (up from 25%)"
    },
    {
        "event_name": "Biden Solar Cell Tariff Hike",
        "legal_authority": "Section 301 (modified)",
        "country_code": "156",
        "hs_chapters": "85",
        "additional_rate": 0.50,
        "effective_date": "2024-08-01",
        "end_date": None,
        "note": "Solar cells: 50% (up from 25%); wafers 50%"
    },
    {
        "event_name": "Universal Baseline Tariff 10%",
        "legal_authority": "IEEPA",
        "country_code": "ALL",
        "hs_chapters": "ALL",
        "additional_rate": 0.10,
        "effective_date": "2025-04-05",
        "end_date": None,
        "note": "10% floor on all imports from all countries"
    },
    {
        "event_name": "Reciprocal Tariff - China (escalated)",
        "legal_authority": "IEEPA",
        "country_code": "156",
        "hs_chapters": "ALL",
        "additional_rate": 0.145,
        "effective_date": "2025-04-09",
        "end_date": None,
        "note": "Additional 14.5% on China on top of universal 10%"
    }
]

df = pd.DataFrame(events)
df.to_csv("data/raw/tariff_events.csv", index=False)
print(f"Saved {len(df)} tariff events to data/raw/tariff_events.csv")