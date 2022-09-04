from flask import Blueprint, render_template, request
from blueprint_posts.dao.postsDAO import PostDAO

postDAO = PostDAO()
posts_blueprint = Blueprint("posts_blueprint",
                            __name__,
                            template_folder="templates"
                            )


@posts_blueprint.route("/")
def page_index():
    posts = postDAO.get_posts_all()
    return render_template("index.html", posts=posts)


@posts_blueprint.route("/posts/<int:post_id>")
def page_post(post_id):
    post = postDAO.get_post_by_pk(post_id)
    comments = postDAO.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments, comments_count=len(comments))


@posts_blueprint.route("/search/")
def page_search():
    s = request.args.get("s")
    if s is None:
        posts = []
    else:
        posts = postDAO.search_for_posts(s)
    return render_template("search.html", posts=posts, posts_count=len(posts))


@posts_blueprint.route("/users/<username>")
def page_user(username):
    posts = postDAO.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, user=username)
