from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


stations = pd.read_csv("data_small/stations.txt", skiprows=17)

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>/")
def api_data(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
        'station': station,
        'date': date,
        'temperature': temperature
    }


@app.route("/api/v1/<station>")
def api_all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="record")
    # print(df)
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def api_yearly_data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    # print(result)
    return result


@app.route("/historical_weather_api/")
def historical_weather_api():
    return render_template('historical_weather_api.html', data=stations.to_html())


@app.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
