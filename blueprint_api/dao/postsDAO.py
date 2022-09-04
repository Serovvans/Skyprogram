import json
import os

from typing import List, Dict


class PostDAO:

    def __init__(self):
        self.posts_path = os.path.join("data", "posts.json")
        self.comments_path = os.path.join("data", "comments.json")

    def load_posts_all(self) -> List[Dict]:
        """Возвращает список всех постов"""

        with open(self.posts_path, "r", encoding="UTF-8") as file:
            posts = json.load(file)

        return posts

    def get_posts_all(self) -> List[Dict]:
        return self.load_posts_all()

    def get_posts_by_user(self, user_name: str) -> List[Dict]:
        """Возвращает список всех постов заданного пользователя"""
        posts = self.get_posts_all()

        if type(user_name) != str:
            raise TypeError("Имя пользователя должно быть строкой")

        users_posts = []
        for post in posts:
            if post["poster_name"] == user_name:
                users_posts.append(post)

        return users_posts

    def get_comments_by_post_id(self, post_id: int) -> List[Dict]:
        """Возвращает список комментариев к посту с pk == post_id"""
        if type(post_id) != int:
            raise TypeError("id поста должен быть целым числом")

        all_posts_id = [post["pk"] for post in self.get_posts_all()]
        if post_id not in all_posts_id:
            raise ValueError("нет поста с таким id")

        with open(self.comments_path, "r", encoding="UTF-8") as file:
            comments = json.load(file)

        posts_comments = []
        for comment in comments:
            if comment["post_id"] == post_id:
                posts_comments.append(comment)

        return posts_comments

    def search_for_posts(self, query: str) -> List[Dict]:
        """Возвращает список постов, содержащий ключевое слово"""
        if type(query) != str:
            raise TypeError("Ключевое слово должно быть строкой")

        posts = self.get_posts_all()
        relevant_posts = []
    
        for post in posts:
            if query.lower() in post["content"].lower():
                relevant_posts.append(post)

        return relevant_posts

    def get_post_by_pk(self, pk: int) -> Dict:
        """Возвращает пост с подходящим pk"""
        if type(pk) != int:
            raise TypeError("pk поста должен быть целым числом")

        posts = self.get_posts_all()
        for post in posts:
            if post["pk"] == pk:
                return post

        raise ValueError("Поста с заданным pk не существует")
