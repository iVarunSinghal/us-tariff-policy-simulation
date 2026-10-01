import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

def clear_existing_data():
    with engine.begin() as conn:
        # Cascade cleanly empties all tables so we can insert fresh without duplicates
        conn.execute(text("TRUNCATE TABLE trade_flows, countries, tariff_schedule, tariff_events, scenario_overrides, scenarios CASCADE;"))
        print("✓ Existing table data cleared")

def load_countries():
    countries = [
        {"country_code": "156", "country_name": "China", "region": "Asia", "is_key_partner": True},
        {"country_code": "484", "country_name": "Mexico", "region": "Americas", "is_key_partner": True},
        {"country_code": "124", "country_name": "Canada", "region": "Americas", "is_key_partner": True},
        {"country_code": "704", "country_name": "Vietnam", "region": "Asia", "is_key_partner": True},
        {"country_code": "356", "country_name": "India", "region": "Asia", "is_key_partner": True},
        {"country_code": "276", "country_name": "Germany", "region": "Europe", "is_key_partner": True},
    ]
    pd.DataFrame(countries).to_sql("countries", engine, if_exists="append", index=False)
    print("✓ Countries loaded")

def load_tariff_schedule():
    path = "data/processed/hts_clean.csv"
    if os.path.exists(path):
        # Force code to be a string so leading zeroes aren't lost
        df = pd.read_csv(path, dtype={"hts_code": str})
        
        # FIX 1: Drop duplicate HTS codes to satisfy the database UNIQUE constraint
        df = df.drop_duplicates(subset=["hts_code"], keep="first")
        
        # FIX 2: Force column2_rate to be strictly numeric (turns text into NULL/NaN)
        df["column2_rate"] = pd.to_numeric(df["column2_rate"], errors="coerce")
        
        df.to_sql("tariff_schedule", engine, if_exists="append", index=False)
        print(f"✓ {len(df)} HTS tariff schedule codes loaded")
    else:
        print("✗ hts_clean.csv not found. Run parse_hts.py first.")

def load_tariff_events():
    path = "data/raw/tariff_events.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        df.to_sql("tariff_events", engine, if_exists="append", index=False)
        print(f"✓ {len(df)} Tariff events loaded")
    else:
        print("✗ tariff_events.csv not found.")

def seed_scenarios():
    scenarios = [
        ("Baseline - Pre-2018", "MFN rates only. No Section 301, no 232.", True),
        ("Phase 1 Deal - 2020", "List 4A reduced to 7.5%; Lists 1-3 remain.", False),
        ("Current - 2026 Active", "All active tariffs: 301, 232, 2025-2026 IEEPA actions.", False),
        ("Escalation - Full 50% China", "Hypothetical: 50% blanket on all Chinese goods.", False),
        ("De-escalation - Deal", "Hypothetical: China deal rolls back to 10% flat.", False),
    ]

    overrides = {
        "Baseline - Pre-2018": [("ALL", "ALL", 0.035)],
        "Phase 1 Deal - 2020": [("156", "85", 0.275), ("156", "84", 0.285), ("156", "ALL", 0.075)],
        "Current - 2026 Active": [("156", "87", 1.025), ("156", "85", 0.50), ("156", "84", 0.50), ("ALL", "ALL", 0.10)],
        "Escalation - Full 50% China": [("156", "ALL", 0.50), ("ALL", "ALL", 0.10)],
        "De-escalation - Deal": [("156", "ALL", 0.10), ("ALL", "ALL", 0.05)],
    }

    with engine.begin() as conn:
        for name, desc, is_base in scenarios:
            res = conn.execute(
                text("INSERT INTO scenarios (scenario_name, description, is_baseline) VALUES (:n, :d, :b) RETURNING scenario_id"),
                {"n": name, "d": desc, "b": is_base}
            )
            scenario_id = res.scalar()

            for c_code, chapter, rate in overrides[name]:
                conn.execute(
                    text("INSERT INTO scenario_overrides (scenario_id, country_code, hs_chapter, tariff_rate) VALUES (:s, :c, :h, :r)"),
                    {"s": scenario_id, "c": c_code, "h": chapter, "r": rate}
                )
    print("✓ 5 Scenarios and overrides seeded")

if __name__ == "__main__":
    print("Loading reference data into PostgreSQL...")
    clear_existing_data()
    load_countries()
    load_tariff_schedule()
    load_tariff_events()
    seed_scenarios()
    print("\n✓ Database setup complete.")