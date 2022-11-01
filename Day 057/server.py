import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.datetime.now().year
    return render_template("example.html", current_year=year)


@app.route("/guess/<string:name>")
def guess(name):
    with requests.get(f"https://api.genderize.io?name={name}&country_id=DE") as response:
        response.raise_for_status()
        data = response.json()
        gender = data["gender"]

    with requests.get(f"https://api.agify.io?name={name}&country_id=US") as response:
        response.raise_for_status()
        data = response.json()
        age = data["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    with requests.get(url) as response:
        response.raise_for_status()
        data = response.json()

    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)
