from flask import Flask
import random

app = Flask(__name__)
rand_num = random.randint(0, 9)


@app.route("/")
def landing_page():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="https://media.giphy.com/media/kfR4CCfebEorm1ljAF/giphy.gif">'


@app.route("/<int:num>")
def user_guess(num):
    if num == rand_num:
        return '<h1 style="color:green";>You found the correct number!</h1>' \
               '<img src="https://media.giphy.com/media/LpcqEAGcYyRA326U2a/giphy.gif">'
    elif num < rand_num:
        return '<h1 style="color:red";>Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/TfLEXiRtYoHUkaPVUk/giphy.gif">'
    else:
        return '<h1 style="color:purple";>Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/YQGhqLUgkcZCRGiNJJ/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
