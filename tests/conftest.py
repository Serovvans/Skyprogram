import pytest

from blueprint_posts.dao.post import Post
from blueprint_api.api import api_blueprint
from flask import Flask


@pytest.fixture()
def simple_post():
    return Post(
        poster_name="hank",
        poster_avatar="https://randus.org/avatars/m/383c7e7e3c3c1818.png",
        pic="https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        content="Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.",
        views_count=187,
        likes_count=67,
        pk=3
    )


@pytest.fixture()
def hanks_posts():
    return [Post(
        poster_name="hank",
        poster_avatar="https://randus.org/avatars/m/383c7e7e3c3c1818.png",
        pic="https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        content="Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.",
        views_count=187,
        likes_count=67,
        pk=3
    ), Post(
        poster_name="hank",
        poster_avatar="https://randus.org/avatars/m/383c7e7e3c3c1818.png",
        pic="https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80",
        content="Очень красивый закат. Стоило выбраться из дома, чтобы посмотреть на него! а где ты был?",
        views_count=166,
        likes_count=76,
        pk=7
    )]


@pytest.fixture()
def app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    return app
