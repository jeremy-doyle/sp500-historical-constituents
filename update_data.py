import pandas as pd

df = pd.read_csv("data/sp500_historical_constituents.csv")
last_update_tickers = df["tickers"].values[-1]

wiki = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
wiki_tickers = wiki["Symbol"].sort_values().drop_duplicates().tolist()
wiki_tickers = ",".join(wiki_tickers)

if last_update_tickers != wiki_tickers:
    last_added_date = pd.to_datetime(wiki["Date added"]).max().strftime("%Y-%m-%d")
    new_row = {"as_of_date": last_added_date, "tickers": wiki_tickers}
    new_row = pd.DataFrame(new_row, index=[0])
    updated = pd.concat([df, new_row], ignore_index=True)
    updated.to_csv("data/sp500_historical_constituents.csv", index=False)
