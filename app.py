from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

# DATA BANDUNG BARAT
tahun_data = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
              2020, 2021, 2022, 2023, 2024, 2025]

penduduk_data = [1522.08, 1545.12, 1567.4, 1588.78, 1609.51, 1629.42,
                 1648.39, 1666.51, 1683.7, 1699.9,
                 1782.19, 1808.42, 1834.23, 1859.64, 1884.19, 1907.82]


@app.route('/')
def home():
    return render_template("index.html",
                           tahun=tahun_data,
                           penduduk=penduduk_data)


@app.route('/predict', methods=['POST'])
def predict():
    tahun_input = int(request.form['tahun'])
    hasil = model.predict([[tahun_input]])

    tahun_baru = tahun_data + [tahun_input]
    penduduk_baru = penduduk_data + [hasil[0]]

    return render_template("index.html",
                           prediksi=f"Prediksi: {hasil[0]:.2f} ribu orang",
                           tahun=tahun_baru,
                           penduduk=penduduk_baru)


if __name__ == "__main__":
    app.run(debug=True)
