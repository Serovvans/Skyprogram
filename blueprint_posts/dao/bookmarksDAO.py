import os
import json

from typing import List
from blueprint_posts.dao.postsDAO import PostDAO
from blueprint_posts.dao.post import Post


class BookmarksDAO:
    """DAO закладок"""
    def __init__(self):
        self.path = os.path.join("data", "bookmarks.json")
        self.postsDAO = PostDAO()

    def load_bookmarks(self) -> List[Post]:
        """Возвращает список постов из закладок пользователя"""

        with open(self.path, "r", encoding="UTF-8") as file:
            bookmarks = json.load(file)

        current_bookmarks = []
        for bookmark in bookmarks:
            current_bookmarks.append(Post(bookmark["poster_name"], bookmark["poster_avatar"], bookmark["pic"],
                                          bookmark["content"], bookmark["views_count"],
                                          bookmark["likes_count"], bookmark["pk"]))

        return current_bookmarks

    def add_bookmark(self, post_id: int):
        """Добавляет пост в закладки"""
        if type(post_id) != int:
            raise TypeError

        post = self.postsDAO.get_post_by_pk(post_id)
        bookmarks = self.load_bookmarks()
        bookmarks.append(post)

        bookmarks_dicts = []
        for bookmark in bookmarks:
            bookmarks_dicts.append({"poster_name": bookmark.poster_name, "poster_avatar": bookmark.poster_avatar,
                                    "pic": bookmark.pic, "content": bookmark.content,
                                    "views_count": bookmark.views_count, "likes_count": bookmark.likes_count,
                                    "pk": bookmark.pk})

        with open(self.path, "w", encoding="UTF-8") as file:
            json.dump(bookmarks_dicts, file)

    def delete_bookmark(self, post_id: int):
        """Удаляет пост из закладок"""
        if type(post_id) != int:
            raise TypeError

        with open(self.path, "r", encoding="UTF-8") as file:
            bookmarks = json.load(file)

        for bookmark in bookmarks:
            if bookmark["pk"] == post_id:
                bookmarks.remove(bookmark)

        with open(self.path, "w", encoding="UTF-8") as file:
            json.dump(bookmarks, file)
