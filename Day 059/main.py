import requests
from flask import Flask, render_template

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
@app.route("/index.html")
def landing_page():
    return render_template("index.html", data=posts)


@app.route("/about.html")
def about_page():
    return render_template("about.html")


@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")


@app.route("/blogpost/<int:postid>")
def blog_page(postid):
    show_post = None
    for post in posts:
        if post["id"] == postid:
            show_post = post
    return render_template("post.html", post=show_post)


if __name__ == "__main__":
    app.run(debug=True)
