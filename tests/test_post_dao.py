import pytest

from postsDAO import PostDAO

postDAO = PostDAO()


def test_get_post_by_user(hanks_posts):

    assert postDAO.get_posts_by_user("hank") == hanks_posts
    assert len(postDAO.get_posts_by_user("kim")) == 0
    assert len(postDAO.get_posts_by_user("larry")) == 2

    with pytest.raises(TypeError):
        postDAO.get_posts_by_user(56.6)


def test_get_comment_by_post_id():

    assert len(postDAO.get_comments_by_post_id(1)) == 4
    assert len(postDAO.get_comments_by_post_id(8)) == 0

    with pytest.raises(ValueError):
        postDAO.get_comments_by_post_id(19)

    with pytest.raises(TypeError):
        postDAO.get_comments_by_post_id("rt")


def test_search_for_posts(simple_post):

    assert postDAO.search_for_posts("ржавые елки") == [simple_post]
    assert len(postDAO.search_for_posts("abcd")) == 0

    with pytest.raises(TypeError):
        postDAO.search_for_posts(57)


def test_get_post_by_pk(simple_post):

    assert postDAO.get_post_by_pk(3) == simple_post

    with pytest.raises(TypeError):
        postDAO.get_post_by_pk("5")

    with pytest.raises(ValueError):
        postDAO.get_post_by_pk(15)
