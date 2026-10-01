import re
import pandas as pd
import os

def parse_hts_schedule(filepath="data/raw/hts_schedule.xlsx"):
    print("Reading Excel file... (this may take a minute)")
    
    # Load data without skipping rows
    df = pd.read_excel(filepath)
    
    # Force rename the first 7 columns by position (standard USITC export structure)
    new_cols = ["hts_code", "indent", "description", "unit", "mfn_rate_raw", "special_rate", "column2_rate"]
    df.columns = new_cols + list(df.columns[7:])
    
    # Keep only what we need and drop empty rows
    df = df[["hts_code", "description", "mfn_rate_raw", "special_rate", "column2_rate"]].dropna(subset=["hts_code"])
    
    def extract_rate(val):
        if pd.isna(val) or str(val).strip().lower() == "free":
            return 0.0
        match = re.search(r"(\d+(\.\d+)?)\s*%", str(val))
        if match:
            return float(match.group(1)) / 100.0
        return 0.035  # Standard fallback for complex mixed rates
        
    df["hts_code"] = df["hts_code"].astype(str).str.replace(".", "", regex=False).str.strip()
    df["mfn_rate"] = df["mfn_rate_raw"].apply(extract_rate)
    df["hts_chapter"] = df["hts_code"].str[:2]
    
    # Filter for targeted chapters (Machinery, Electronics, Vehicles, Furniture, Apparel)
    valid_chapters = ["84", "85", "87", "94", "61", "62"]
    df_clean = df[df["hts_chapter"].isin(valid_chapters)].copy()
    
    os.makedirs("data/processed", exist_ok=True)
    
    output_cols = ["hts_code", "description", "hts_chapter", "mfn_rate", "special_rate", "column2_rate"]
    df_clean[output_cols].to_csv("data/processed/hts_clean.csv", index=False)
    print(f"✓ HTS schedule parsed - {len(df_clean)} codes across chapters {valid_chapters}")

if __name__ == "__main__":
    parse_hts_schedule()