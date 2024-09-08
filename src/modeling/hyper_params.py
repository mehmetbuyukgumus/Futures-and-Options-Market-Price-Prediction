gbr_param_grid = {
    "n_estimators": [100,200],
    "learning_rate": [0.01, 0.05],
    'max_depth': [3, 4, 5],
    "min_samples_split": [10, 20],
    "min_samples_leaf": [2, 3, 4],
    "subsample": [0.8, 0.9],
}

# ridge_param_grid = {
#     'alpha': [0.01, 0.1, 1.0, 10.0, 100.0],
#     'fit_intercept': [True, False]
# }

# lasso_param_grid = {
#     'alpha': [0.01, 0.1, 1.0, 10.0, 100.0],
#     'fit_intercept': [True, False]
# }

# rf_param_grid = {
#     'n_estimators': [100, 300, 500, 1000],
#     'max_depth': [None, 10, 20, 30],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4],
#     'max_features': ['auto', 'sqrt', 'log2'],
#     'bootstrap': [True, False]
# }

# xgbr_param_grid = {
#     'n_estimators': [100, 500, 1000],
#     'learning_rate': [0.01, 0.05, 0.1],
#     'max_depth': [3, 5, 7],
#     # 'min_child_weight': [1, 3, 5],
#     # 'subsample': [0.8, 1.0],
#     # 'colsample_bytree': [0.8, 1.0],
#     # 'gamma': [0, 0.1, 0.3],
#     # 'reg_alpha': [0, 0.01, 0.1],
#     # 'reg_lambda': [1, 1.5, 2]
# }

# lgbmr_param_grid = {
#     'n_estimators': [100, 500, 1000],
#     'learning_rate': [0.01, 0.05, 0.1],
#     'max_depth': [3, 5, 7, -1],
#     'num_leaves': [31, 50, 100],
#     'min_child_samples': [10, 20, 30],
#     'subsample': [0.7, 0.8, 1.0],
#     'colsample_bytree': [0.7, 0.8, 1.0],
#     'reg_alpha': [0.0, 0.1, 0.5],
#     'reg_lambda': [0.0, 1.0, 5.0]
# }

# catboost_param_grid = {
#     'depth': [4, 6, 8, 10],
#     'learning_rate': [0.01, 0.05, 0.1],
#     'iterations': [500, 1000],
#     'l2_leaf_reg': [1, 3, 5, 7],
#     'bagging_temperature': [0.1, 0.5, 1.0]
# }

# lineer_param_grid = {
#     'alpha': [0.01, 0.1, 1.0, 10.0, 100.0],
#     'fit_intercept': [True, False]
# }
