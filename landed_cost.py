import os
import pandas as pd
from dataclasses import dataclass

# Statutory US Customs Parameters (FY 2026)
FREIGHT_PCT = 0.035       # 3.5% sea freight estimate
INSURANCE_PCT = 0.005     # 0.5% marine insurance
MPF_RATE = 0.003464       # Merchandise Processing Fee (ad valorem component)
MPF_MIN = 33.58           # Statutory minimum per entry for FY2026
MPF_MAX = 651.50          # Statutory maximum per entry for FY2026
HMF_RATE = 0.00125        # Harbor Maintenance Fee (0.125%)

@dataclass
class LandedCostResult:
    scenario: str
    country: str
    hs_chapter: str
    fob_value: float
    freight: float
    insurance: float
    cif_value: float
    tariff_rate: float
    tariff_amount: float
    mpf: float
    hmf: float
    landed_cost: float
    importer_price: float
    wholesale_price: float
    consumer_price: float
    tariff_passthrough: float

def calculate_landed_cost(
    fob_value: float,
    tariff_rate: float,
    scenario: str,
    country: str = "China",
    hs_chapter: str = "85",
    importer_margin: float = 0.20,
    wholesaler_margin: float = 0.15,
    retailer_margin: float = 0.40
) -> LandedCostResult:
    freight = fob_value * FREIGHT_PCT
    insurance = (fob_value + freight) * INSURANCE_PCT
    cif_value = fob_value + freight + insurance
    
    tariff_amount = cif_value * tariff_rate
    mpf = max(MPF_MIN, min(MPF_MAX, cif_value * MPF_RATE))
    hmf = cif_value * HMF_RATE
    
    landed_cost = cif_value + tariff_amount + mpf + hmf
    importer_price = landed_cost * (1.0 + importer_margin)
    wholesale_price = importer_price * (1.0 + wholesaler_margin)
    consumer_price = wholesale_price * (1.0 + retailer_margin)
    
    passthrough = tariff_amount / consumer_price if consumer_price > 0 else 0.0

    return LandedCostResult(
        scenario=scenario,
        country=country,
        hs_chapter=hs_chapter,
        fob_value=round(fob_value, 2),
        freight=round(freight, 2),
        insurance=round(insurance, 2),
        cif_value=round(cif_value, 2),
        tariff_rate=tariff_rate,
        tariff_amount=round(tariff_amount, 2),
        mpf=round(mpf, 2),
        hmf=round(hmf, 2),
        landed_cost=round(landed_cost, 2),
        importer_price=round(importer_price, 2),
        wholesale_price=round(wholesale_price, 2),
        consumer_price=round(consumer_price, 2),
        tariff_passthrough=round(passthrough * 100, 2)
    )

def run_scenarios_export():
    scenario_rates = {
        "Baseline - Pre-2018": 0.035,
        "Phase 1 Deal - 2020": 0.075,
        "Current - 2026 Active": 0.535,
        "Escalation - Full 50% China": 0.60,
        "De-escalation - Deal": 0.135
    }
    
    fob = 100.0
    country = "China"
    hs = "85"
    
    baseline = calculate_landed_cost(fob, scenario_rates["Baseline - Pre-2018"], "Baseline", country, hs)
    rows = []
    
    for name, rate in scenario_rates.items():
        res = calculate_landed_cost(fob, rate, name, country, hs)
        delta_usd = res.consumer_price - baseline.consumer_price
        delta_pct = (delta_usd / baseline.consumer_price) * 100
        
        rows.append({
            "scenario": res.scenario,
            "country": res.country,
            "hs_chapter": res.hs_chapter,
            "fob_value": res.fob_value,
            "cif_value": res.cif_value,
            "tariff_rate_pct": round(res.tariff_rate * 100, 1),
            "tariff_amount_usd": res.tariff_amount,
            "mpf_hmf_usd": round(res.mpf + res.hmf, 2),
            "landed_cost_usd": res.landed_cost,
            "consumer_price_usd": res.consumer_price,
            "consumer_price_delta_usd": round(delta_usd, 2),
            "consumer_price_delta_pct": round(delta_pct, 2),
            "tariff_passthrough_pct": res.tariff_passthrough
        })
        
    os.makedirs("data/exports", exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv("data/exports/scenario_comparison.csv", index=False)
    print(f"✓ Scenario comparisons exported ({len(df)} scenarios)")
    print(df[["scenario", "tariff_rate_pct", "consumer_price_usd", "consumer_price_delta_pct"]])

if __name__ == "__main__":
    run_scenarios_export()