from typing import List


class Post:
    def __init__(self, poster_name: str, poster_avatar: str,
                 pic: str, content: str, views_count: int, likes_count: int, pk: int):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk
        self.content_str = self.content

        self.replace_tags_to_a()

    def replace_tags_to_a(self) -> None:
        content = self.content.split()

        for i in range(len(content)):
            if content[i].startswith("#"):
                content[i] = f"<a href='/tag/{content[i][1:]}'>{content[i]}</a>"

        self.content = " ".join(content)

    def get_posts_tags(self) -> List[str]:
        words = self.content_str.split()
        tags = []

        for word in words:
            if word.startswith("#"):
                tags.append(word)

        return tags

    def __eq__(self, other):
        return ((self.poster_name == other.poster_name) and
                (self.poster_avatar == other.poster_avatar) and
                (self.pic == other.pic) and
                (self.content == other.content) and
                (self.views_count == other.views_count) and
                (self.likes_count == other.likes_count) and (self.pk == other.pk))
