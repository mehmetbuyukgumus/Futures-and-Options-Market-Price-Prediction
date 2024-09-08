from joblib import load
import numpy as np

def prediction(price):
    model = load("src/modeling/model-file.joblib")
    price = np.array(price).reshape(1,-1)
    res_prediction = model.predict(price)
    return res_prediction