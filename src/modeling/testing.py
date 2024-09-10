from prices.prepared_data import historical_prices
from modeling.hyper_params import *
from modeling.models import regressors
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from joblib import dump
import pandas as pd


def prep_data_of_model():
    data = historical_prices("KOZAL.IS", "KOZAA.IS", "2020-07-08", "2024-09-10")
    data.dropna(inplace=True)
    return data


def scaler(train, test):
    scaler = StandardScaler()
    scaled_fit = scaler.fit_transform(train)
    scaled_transform = scaler.transform(test)
    return scaled_fit, scaled_transform


def test_split_data(data):
    X = data["X"].to_frame()
    y = data["y"].to_frame()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    X_train = X_train.values.reshape(-1, 1)
    X_test = X_test.values.reshape(-1, 1)
    y_train = y_train.values.reshape(-1, 1)
    y_test = y_test.values.reshape(-1, 1)
    return X, y, X_train, X_test, y_train, y_test


def testing_result_of_model(X_train, X_test, y_train, y_test):
    r2_Score = []
    mae_Score = []
    mse_Score = []
    model_name = []
    for name, regressor, param in regressors:
        model = regressor
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2_Score.append(r2_score(y_test, y_pred))
        mae_Score.append(mean_absolute_error(y_test, y_pred))
        mse_Score.append(mean_squared_error(y_test, y_pred))
        model_name.append(name)
    result = pd.DataFrame(
        {
            "Model": model_name,
            "r2_Score": r2_Score,
            "mae_Score": mae_Score,
            "mse_Score": mse_Score,
        },
    )
    return result, model, name, regressor, param


def grid_seach_cv(X, y, X_train, X_test, y_train, y_test, model, name, regressor, param):
    r2_Score_new = []
    mae_Score_new = []
    mse_Score_new = []
    model_name_new = []
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param,
        cv=3,
        scoring="neg_mean_absolute_error",
        verbose=1,
        n_jobs=-1,
    )
    grid_search.fit(X_train, y_train)
    model_final = regressor.set_params(**grid_search.best_params_).fit(X, y)
    y_pred_final = model_final.predict(X_test)

    r2_Score_new.append(r2_score(y_test, y_pred_final))
    mae_Score_new.append(mean_absolute_error(y_test, y_pred_final))
    mse_Score_new.append(mean_squared_error(y_test, y_pred_final))
    model_name_new.append(name)
    result_new = pd.DataFrame(
        {
            "r2_Score_new": r2_Score_new,
            "mae_Score_new": mae_Score_new,
            "mse_Score_new": mse_Score_new,
        },
    )
    return result_new


data = prep_data_of_model()
X, y, X_train, X_test, y_train, y_test = test_split_data(data)
# X_train, X_test = scaler(X_train, X_test)
result, model, name, regressor, param = testing_result_of_model(X_train, X_test, y_train, y_test)
result_new = grid_seach_cv(X, y, X_train, X_test, y_train, y_test, model, name, regressor, param)

print(pd.concat([result, result_new], axis=1))
dump(model, "src/modeling/model-file.joblib")

