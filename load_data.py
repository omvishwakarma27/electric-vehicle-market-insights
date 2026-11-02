from pathlib import Path
import sqlite3
import pandas as pd

csv_path = Path("ev_market_train.csv")
db_path = Path("ev_market.db")

if not csv_path.exists():
    raise FileNotFoundError("Place ev_market_train.csv beside load_data.py before running this script.")

df = pd.read_csv(csv_path)
print(f"Loaded {len(df):,} rows and {len(df.columns)} columns.")
print("Missing values in most affected columns:")
print(df.isna().sum().sort_values(ascending=False).head(10))

with sqlite3.connect(db_path) as con:
    df.to_sql("ev_market", con, if_exists="replace", index=False)
    con.execute("CREATE INDEX IF NOT EXISTS idx_manufacturer ON ev_market(manufacturer)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_region ON ev_market(market_region)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_model_year ON ev_market(model_year)")
    count = con.execute("SELECT COUNT(*) FROM ev_market").fetchone()[0]

print(f"Created {db_path.resolve()}")
print(f"Rows verified in database: {count:,}")
