import yfinance as yf
import pandas as pd

def historical_prices(company_name1, company_name2, start_date, end_date):
    conmapany_prices1 = yf.Ticker(company_name1)
    conmapany_prices2 = yf.Ticker(company_name2)
    historical_conmapany_prices1 = conmapany_prices1.history(start = start_date, end = end_date, interval="1d")
    historical_conmapany_prices2 = conmapany_prices2.history(start = start_date, end = end_date, interval="1d")
    final_df = pd.DataFrame({"X": historical_conmapany_prices1["Close"],
                             "y": historical_conmapany_prices2["Close"]})
    final_df = final_df.reset_index()
    final_df['Date'] = pd.to_datetime(final_df['Date']).dt.strftime('%d.%m.%y')
    return final_df