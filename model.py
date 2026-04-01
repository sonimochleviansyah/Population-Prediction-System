from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "Tahun": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
              2020, 2021, 2022, 2023, 2024, 2025],
    "Penduduk": [1522.08, 1545.12, 1567.4, 1588.78, 1609.51, 1629.42,
                 1648.39, 1666.51, 1683.7, 1699.9,
                 1782.19, 1808.42, 1834.23, 1859.64, 1884.19, 1907.82]
}

df = pd.DataFrame(data)

X = df[['Tahun']]
y = df['Penduduk']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))


y_pred = model.predict(X)

print("MAE:", mean_absolute_error(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))
print("R2:", r2_score(y, y_pred))

print("Model berhasil dibuat!")
