import logging

from flask import Blueprint, jsonify
from blueprint_api.dao.postsDAO import PostDAO


api_logger = logging.getLogger("api")
fileHandler = logging.FileHandler(filename="api.log")
fileHandler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
api_logger.addHandler(fileHandler)

postsDAO = PostDAO()

api_blueprint = Blueprint("api_blueprint",
                          __name__)


@api_blueprint.route("/api/posts")
def api_posts():
    posts = postsDAO.get_posts_all()
    api_logger.info(f"api/posts")
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_id>")
def api_post(post_id):
    post = postsDAO.get_post_by_pk(post_id)
    api_logger.info(f"api/posts/{post_id}")
    return jsonify(post)
