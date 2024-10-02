from joblib import load
from modeling.testing import *
from modeling.pairs import pairs
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
from warnings import filterwarnings
filterwarnings("ignore")

def prediction():
    # model = load("src/modeling/model-file.joblib")
    companies = []
    pred_results = []
    for i in range(len(pairs)):
        ticker = yf.Ticker(f"{pairs[i][0]}.IS")
        history = ticker.history(start="2024-07-08", end=dt.datetime.now().date())
        price = np.array(history["Close"][-1]).reshape(1,-1)
        data = prep_data_of_model(f"{pairs[i][0]}.IS", f"{pairs[i][1]}.IS")
        X, y, X_train, X_test, y_train, y_test = test_split_data(data)
        result, model, name, regressor, param = testing_result_of_model(X_train, X_test, y_train, y_test)
        result_new, model_final = grid_seach_cv(X, y, X_train, X_test, y_train, y_test, model, name, regressor, param)
        # model = load("src/modeling/model-file.joblib")
        res_prediction = model_final.predict(price)
        companies.append(pairs[i][1])
        pred_results.append(res_prediction)
    final_table = pd.DataFrame({
        "Companies" : companies,
        "Tahmin Sonucları": pred_results
    })
    final_table.to_excel("output.xlsx", index=False)