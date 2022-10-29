from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_fun():
        return "<b>" + function() + "</b>"
    return wrapper_fun


def make_emphasis(function):
    def wrapper_fun():
        return "<em>" + function() + "</em>"
    return wrapper_fun


def make_underlined(function):
    def wrapper_fun():
        return "<u>" + function() + "</u>"
    return wrapper_fun


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye"


@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}!"


if __name__ == "__main__":
    app.run(debug=True)