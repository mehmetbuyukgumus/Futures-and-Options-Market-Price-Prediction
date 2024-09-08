from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from modeling.hyper_params import *


regressors = [
    # ("Lasso", Lasso(), lasso_param_grid),
    # ("Ridge", Ridge(), ridge_param_grid),
    # ("RandomForest", RandomForestRegressor(), rf_param_grid),
    ("GradientBoosting", GradientBoostingRegressor(), gbr_param_grid),
    # ("XGBR", XGBRegressor(), xgbr_param_grid),
    # ("LGBMR", LGBMRegressor(),lgbmr_param_grid),
    # ("CatBoost", CatBoostRegressor(), catboost_param_grid),
    # ("LineerReg",LinearRegression(), lineer_param_grid) 
]