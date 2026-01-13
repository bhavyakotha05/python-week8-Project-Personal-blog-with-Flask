from flask import redirect, url_for, flash, request
from flask_login import login_required, current_user

from app import db
from app.comments import comments_bp
from app.comments.forms import CommentForm
from app.models import Comment, Post


# -------------------------
# Add Comment
# -------------------------
@comments_bp.route("/add/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            author=current_user,
            post=post
        )
        db.session.add(comment)
        db.session.commit()
        flash("Comment added successfully!", "success")
    else:
        flash("Failed to add comment.", "danger")

    return redirect(url_for("posts.view", post_id=post.id))


# -------------------------
# Delete Comment
# -------------------------
@comments_bp.route("/delete/<int:comment_id>", methods=["POST"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Allow delete if author or post author
    if comment.author != current_user and comment.post.author != current_user:
        flash("You are not allowed to delete this comment.", "danger")
        return redirect(url_for("main.home"))

    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    flash("Comment deleted.", "info")
    return redirect(url_for("posts.view", post_id=post_id))
