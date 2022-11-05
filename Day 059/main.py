import requests
from flask import Flask, render_template, request

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def landing_page():
    return render_template("index.html", data=posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/blogpost/<int:postid>")
def blog_page(postid):
    show_post = None
    for post in posts:
        if post["id"] == postid:
            show_post = post
    return render_template("post.html", post=show_post)


if __name__ == "__main__":
    app.run(debug=True)
