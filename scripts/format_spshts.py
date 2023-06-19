# ====formats dates to yyyy-mm-dd in the spreadsheets, and drops the null columns=====
import pandas as pd

def format_date_df(year):
    df = pd.read_csv(
        f"C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_adv_data20{year}.csv")
    df = df.dropna(axis=1, how='any')
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    # df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df.to_csv(f"nhl_dropped_20{year}.csv")


for year in [18, 19, 20, 21, 22]:
    format_date_df(year)
