import logging

from flask import Blueprint, jsonify
from blueprint_api.dao.postsDAO import PostDAO


logging.basicConfig(level=logging.INFO, filename="api.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

postsDAO = PostDAO()

api_blueprint = Blueprint("api_blueprint",
                          __name__)


@api_blueprint.route("/api/posts")
def api_posts():
    posts = postsDAO.get_posts_all()
    logging.info(f"api/posts")
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_id>")
def api_post(post_id):
    post = postsDAO.get_post_by_pk(post_id)
    logging.info(f"api/posts/{post_id}")
    return jsonify(post)
