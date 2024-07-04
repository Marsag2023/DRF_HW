import re

from rest_framework.serializers import ValidationError


class UrlVideoValidator:
    """
    Проверка на отсутствие в уроках ссылок на сторонние ресурсы, кроме youtube.com.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        value_test = dict(value).get(self.field)
        match = re.match(r"^https://www.youtube.com/", value_test)
        print(match)
        if not match:
            raise ValidationError("Можно ссылаться только на видео с youtube.com")
