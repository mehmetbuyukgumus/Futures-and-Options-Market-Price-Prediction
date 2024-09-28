from modeling.prediction import prediction
from warnings import filterwarnings
from modeling.pairs import pairs
import yfinance as yf
import datetime as dt
filterwarnings("ignore")


def main():
    for i in range(len(pairs)):
        for e in range(0,2):
            comp_ticker = yf.Ticker(pairs[i][e])
            historical_data = comp_ticker.history(start= "2020-07-08", end=dt.datetime.today().now().date(), interval="1d")
            current_price = historical_data["Close"].iloc[-1]
            target_price = prediction(current_price)
            print(target_price)


if __name__ == "__main__":
        main()
