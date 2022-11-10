from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from credentials import *
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top10-movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), unique=False, nullable=False)


class MovieEdit(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.6", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


db.create_all()


@app.route("/")
def home():
    # movies = db.session.query(Movie).all()
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieEdit()
    if form.validate_on_submit():
        movie_id = request.args.get("id")
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for("home"))
    movie_id = request.args.get("id")
    edit_movie = Movie.query.get(movie_id)
    return render_template("edit.html", form=form, movie=edit_movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    delete_movie = Movie.query.get(movie_id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        title = request.form["title"]
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}&page=1"
        response = requests.get(url)
        response.raise_for_status()
        movie_list = response.json()["results"]
        return render_template("select.html", movies=movie_list)
    return render_template("add.html", form=form)


@app.route("/select")
def select():
    id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    title = data["original_title"]
    img_url = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    year = data["release_date"]
    description = data["overview"]

    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        img_url=img_url
    )
    db.session.add(new_movie)
    db.session.commit()
    movie_id = Movie.query.filter_by(title=title).first().id

    return redirect(url_for("edit", id=movie_id))


if __name__ == '__main__':
    app.run(debug=True)
