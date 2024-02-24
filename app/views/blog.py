import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.models import User


blog = Blueprint("blog", __name__, url_prefix="/blog")

@blog.route("/")
def blog_index():
    return "This is the blog index page."

@blog.route("/<int:post_id>")
def blog_show(post_id):
    return f"This is the blog post with id {post_id}."

@blog.route("/<int:post_id>/edit")
def blog_edit(post_id):
    return f"This is the edit page for post {post_id}."

@blog.route("/<int:post_id>/delete")
def blog_delete(post_id):
    return f"This deletes the post with id {post_id}."

@blog.route("/create", methods=("GET", "POST"))
def blog_create():
    if request.method == "POST":
        data = request.get_json()
        post_title = data["title"]
        post_content = data["content"]
        blog = BlogPost(title=post_title, content=post_content)
        db.session.add(course)
        db.session.commit()
