from flask import render_template
from app.posts import posts_bp
from app.models import Post

@posts_bp.route("/posts")
def posts_list():
    posts = Post.query.all()
    return render_template("posts/post_detail.html", posts=posts)
