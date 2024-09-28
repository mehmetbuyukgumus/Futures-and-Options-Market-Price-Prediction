from joblib import load
from modeling.pairs import companies
import numpy as np
import os


def prediction(price):
    dir = "src/models_joblib_files/"
    for company in companies:
        model_file_name = [
            model
            for model in os.listdir(dir)
            if model.startswith(company) and os.path.isfile(os.path.join(dir, model))
        ]
        model_file_name_str = "".join(model_file_name)
        model_file_name_str = model_file_name_str.strip("[]'")
        model = load(f"{dir}{model_file_name_str}")
        price = np.array(price).reshape(1, -1)
        res_prediction = model.predict(price)
        return res_prediction
