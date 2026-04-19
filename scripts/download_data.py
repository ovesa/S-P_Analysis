import yfinance as yf

tickers = ["XLK","XLF","XLE","XLV","XLC","XLY","XLP","XLI","XLB","XLU","XLRE"]

for ticker in tickers:
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, start="2018-01-01", end="2026-04-01")
    df.to_csv(f"data/{ticker}.csv")
    print(f"  Saved data/{ticker}.csv")

