import pandas as pd
import matplotlib.pyplot as plt
from prices.prepared_data import historical_prices
from modeling.prediction import prediction
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")


def data_for_vis():
    main_data = historical_prices("PGSUS.IS", "THYAO.IS", "2022-01-01", "2024-08-31")
    main_data = main_data.dropna()
    prep_cols = []
    for i in main_data["X"]:
        prep_cols.append(prediction(i))
    main_data["prep_cols"] = prep_cols
    main_data["prep_cols"] = main_data["prep_cols"].astype(float)
    return main_data


main_data = data_for_vis()

plt.scatter(main_data["y"], main_data.index, label="Gerçek Değerler", s=10)
plt.scatter(main_data["prep_cols"], main_data.index, label="Tahmin Değerleri", s=10)

plt.xlim(0, 300)
plt.ylim(0, 500)

plt.legend()
plt.show()