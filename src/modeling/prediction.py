from joblib import load
from modeling.pairs import companies
import numpy as np
import os

os.chdir("/Users/mehmetbuyukgumus/Desktop/viop/src")

def prediction():
    for company in companies:
        dir = "models_joblib_files/"
        model_file_name = [model for model in os.listdir(dir) if model.startswith(company)]
        model_file_name_str = "".join(model_file_name)
        model_file_name_str = model_file_name_str.strip("[]'")
        model = load(f"models_joblib_files/{model_file_name_str}")
        print(model)
        # price = np.array(price).reshape(1,-1)
        # res_prediction = model.predict(price)
        # return res_prediction
        
        
prediction()