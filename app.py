from flask import Flask, render_template, request, abort
app = Flask(__name__)
from functions import get_posts, get_post,list_c, search_user


@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:postid>")
def posts(postid):
    post = get_post(postid)
    comment=list_c(postid)
    return render_template("post.html", post=post,comment=comment)
    # return "Post not found", 404


@app.route("/search/")
def search_post():
    posts = get_posts()
    word = request.args.get('s')
    if not word:
        abort(400)
    list_posts = []
    for post in posts:
        if word in post["content"]:
            list_posts.append(post)

    return render_template("search.html", posts=list_posts)


@app.route("/users/<username>")
def search_user(username):
    posts =search_user(username)
    return render_template("user-feed.html", posts=posts)



app.run(debug=True)

