import pandas as pd
from rules import categorize
from db import insert

def process_file(file_path):

    df = pd.read_csv(file_path)

    df.columns = [c.strip() for c in df.columns]

    date_col = None
    desc_col = None
    amount_col = None

    for c in df.columns:
        if "date" in c.lower() and date_col is None:
            date_col = c
        if "description" in c.lower() or "merchant" in c.lower():
            desc_col = c
        if "amount" in c.lower():
            amount_col = c

    print("USING COLUMNS:", date_col, desc_col, amount_col)

    if not all([date_col, desc_col, amount_col]):
        print("BAD CSV FORMAT")
        return

    for _, row in df.iterrows():

        date = str(row[date_col]).strip()
        merchant = str(row[desc_col]).strip()

        try:
            amount = float(str(row[amount_col]).replace(",", ""))
        except:
            continue

        category = categorize(merchant)

        source_id = f"{date}-{merchant}-{amount}"

        insert((date, merchant, amount, category, source_id))

    print(f"Processed {file_path}")