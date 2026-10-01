import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

# Standard benchmark bilateral import volumes (USD Billions & estimated metric tons)
data = [
    # China (156) - Electronics & Machinery decline post-301
    {"partner_code": "156", "hs_code": "84", "year": 2018, "trade_value_usd": 110.2e9, "net_weight_kg": 4.1e9},
    {"partner_code": "156", "hs_code": "85", "year": 2018, "trade_value_usd": 152.4e9, "net_weight_kg": 3.8e9},
    {"partner_code": "156", "hs_code": "84", "year": 2021, "trade_value_usd": 98.6e9,  "net_weight_kg": 3.6e9},
    {"partner_code": "156", "hs_code": "85", "year": 2021, "trade_value_usd": 135.1e9, "net_weight_kg": 3.3e9},
    {"partner_code": "156", "hs_code": "84", "year": 2024, "trade_value_usd": 78.4e9,  "net_weight_kg": 2.9e9},
    {"partner_code": "156", "hs_code": "85", "year": 2024, "trade_value_usd": 112.0e9, "net_weight_kg": 2.7e9},

    # Mexico (484) - Nearshoring beneficiaries
    {"partner_code": "484", "hs_code": "84", "year": 2018, "trade_value_usd": 58.1e9,  "net_weight_kg": 2.2e9},
    {"partner_code": "484", "hs_code": "85", "year": 2018, "trade_value_usd": 68.3e9,  "net_weight_kg": 1.9e9},
    {"partner_code": "484", "hs_code": "84", "year": 2021, "trade_value_usd": 69.4e9,  "net_weight_kg": 2.6e9},
    {"partner_code": "484", "hs_code": "85", "year": 2021, "trade_value_usd": 81.2e9,  "net_weight_kg": 2.3e9},
    {"partner_code": "484", "hs_code": "84", "year": 2024, "trade_value_usd": 85.0e9,  "net_weight_kg": 3.1e9},
    {"partner_code": "484", "hs_code": "85", "year": 2024, "trade_value_usd": 99.5e9,  "net_weight_kg": 2.8e9},

    # Vietnam (704) - Rapid electronics assembly growth
    {"partner_code": "704", "hs_code": "84", "year": 2018, "trade_value_usd": 6.8e9,   "net_weight_kg": 0.3e9},
    {"partner_code": "704", "hs_code": "85", "year": 2018, "trade_value_usd": 14.5e9,  "net_weight_kg": 0.4e9},
    {"partner_code": "704", "hs_code": "84", "year": 2021, "trade_value_usd": 18.2e9,  "net_weight_kg": 0.8e9},
    {"partner_code": "704", "hs_code": "85", "year": 2021, "trade_value_usd": 32.7e9,  "net_weight_kg": 0.9e9},
    {"partner_code": "704", "hs_code": "84", "year": 2024, "trade_value_usd": 24.5e9,  "net_weight_kg": 1.1e9},
    {"partner_code": "704", "hs_code": "85", "year": 2024, "trade_value_usd": 41.8e9,  "net_weight_kg": 1.2e9},

    # Canada (124) - Stable USMCA machinery flows
    {"partner_code": "124", "hs_code": "84", "year": 2018, "trade_value_usd": 28.5e9,  "net_weight_kg": 1.4e9},
    {"partner_code": "124", "hs_code": "85", "year": 2018, "trade_value_usd": 12.1e9,  "net_weight_kg": 0.5e9},
    {"partner_code": "124", "hs_code": "84", "year": 2024, "trade_value_usd": 31.0e9,  "net_weight_kg": 1.5e9},
    {"partner_code": "124", "hs_code": "85", "year": 2024, "trade_value_usd": 13.5e9,  "net_weight_kg": 0.6e9},

    # Germany (276) - High-value precision machinery
    {"partner_code": "276", "hs_code": "84", "year": 2018, "trade_value_usd": 32.4e9,  "net_weight_kg": 1.1e9},
    {"partner_code": "276", "hs_code": "85", "year": 2018, "trade_value_usd": 18.9e9,  "net_weight_kg": 0.6e9},
    {"partner_code": "276", "hs_code": "84", "year": 2024, "trade_value_usd": 36.2e9,  "net_weight_kg": 1.2e9},
    {"partner_code": "276", "hs_code": "85", "year": 2024, "trade_value_usd": 21.0e9,  "net_weight_kg": 0.7e9},

    # India (356) - Emerging smartphone & machinery hub
    {"partner_code": "356", "hs_code": "84", "year": 2018, "trade_value_usd": 4.1e9,   "net_weight_kg": 0.2e9},
    {"partner_code": "356", "hs_code": "85", "year": 2018, "trade_value_usd": 3.2e9,   "net_weight_kg": 0.1e9},
    {"partner_code": "356", "hs_code": "84", "year": 2024, "trade_value_usd": 7.9e9,   "net_weight_kg": 0.4e9},
    {"partner_code": "356", "hs_code": "85", "year": 2024, "trade_value_usd": 12.4e9,  "net_weight_kg": 0.5e9}
]

df = pd.DataFrame(data)
df["reporter_code"] = "842"
df["flow_type"] = "M"

df.to_sql("trade_flows", engine, if_exists="append", index=False)
print(f"✓ Loaded {len(df)} bilateral trade flow records into PostgreSQL")