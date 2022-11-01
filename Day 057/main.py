import requests
from post import Post
from flask import Flask, render_template

app = Flask(__name__)
post_list = []
with requests.get("https://api.npoint.io/c790b4d5cab58020d391") as response:
    response.raise_for_status()
    data = response.json()
    for post in data:
        new_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_list.append(new_post)


@app.route('/')
def home():
    return render_template("index.html", posts=post_list)


@app.route('/post/<int:postid>')
def blogpost(postid):
    show_post = None
    for post in post_list:
        if post.id == postid:
            show_post = post
    return render_template("post.html", post=show_post)


if __name__ == "__main__":
    app.run(debug=True)
