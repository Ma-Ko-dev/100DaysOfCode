from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index.html")
@app.route("/")
def landing_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    pw = request.form["password"]
    return f"<h1>Name: {name}, Password: {pw}</h1>"


if __name__ == "__main__":
    app.run(debug=True)