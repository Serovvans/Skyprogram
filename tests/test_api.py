import pytest


def test_posts(app):
    response = app.test_client().get("api/posts")
    assert type(response.json) == list
    assert all(set(post.keys()) == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
                                    "pk"} for post in response.json)


def test_posts_post_id(app):
    response = app.test_client().get("api/posts/1")
    assert type(response.json) == dict
    assert set(response.json.keys()) == {"poster_name", "poster_avatar", "pic", "content", "views_count",
                                         "likes_count", "pk"}
