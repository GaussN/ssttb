from django.db.models.query import QuerySet, Q
from main.models import *
from education.models import *


class SearchUtil:
    def __init__(self, request: str):
        self.__request = request

    def __repr__(self):
        return f"{self.__class__.__name__}(request={self.__request})"

    def search(self):
        result = {
            'lessons': self.__search_in_lessons(),
            'tests': self.__search_in_tests(),
            'media': self.__search_in_media(),
        }
        return result

    def __search_in_lessons(self) -> QuerySet:
        return Lesson.objects.filter(
            Q(topic__icontains=self.__request) |
            Q(page__icontains=self.__request)
        )

    def __search_in_tests(self) -> QuerySet:
        return Test.objects.filter(
            Q(topic__icontains=self.__request) |
            Q(test_json__icontains=self.__request.encode('unicode-escape').decode())
        )

    def __search_in_media(self) -> QuerySet:
        return Media.objects.filter(header__icontains=self.__request)
