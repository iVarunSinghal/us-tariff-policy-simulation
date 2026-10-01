import pandas as pd
from landed_cost import calculate_landed_cost
import itertools

def run_sensitivity_grid():
    fob_value = 100.0
    tariff_rates = [0.0, 0.075, 0.10, 0.25, 0.50, 0.75, 1.00]
    imp_margins = [0.10, 0.15, 0.20, 0.25, 0.30]
    
    rows = []
    for rate, margin in itertools.product(tariff_rates, imp_margins):
        res = calculate_landed_cost(fob_value, rate, "Grid", "China", "85", importer_margin=margin)
        baseline_res = calculate_landed_cost(fob_value, 0.0, "Baseline", "China", "85", importer_margin=margin)
        
        rows.append({
            "tariff_rate_pct": f"{int(rate * 100)}%",
            "importer_margin_pct": f"{int(margin * 100)}%",
            "consumer_price": res.consumer_price,
            "tariff_cost_to_consumer": round(res.tariff_amount * (1 + margin) * 1.15 * 1.40, 2),
            "price_vs_zero_tariff_pct": round(((res.consumer_price / baseline_res.consumer_price) - 1) * 100, 1)
        })

    df = pd.DataFrame(rows)
    df.to_csv("data/exports/sensitivity_grid.csv", index=False)
    print(f"✓ Sensitivity grid exported ({len(df)} scenarios)")

if __name__ == "__main__":
    run_sensitivity_grid()