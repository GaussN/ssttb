import json
from typing import Set

from django.db.models.query import QuerySet

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

    def __search_in_lesson_topics(self) -> QuerySet | None:
        return Lesson.objects.filter(topic__icontains=self.__request)

    def __search_in_lesson_texts(self) -> QuerySet | None:
        return Lesson.objects.filter(page__icontains=self.__request)

    def __search_in_lessons(self) -> Set:
        return set(self.__search_in_lesson_topics()) | set(self.__search_in_lesson_texts())

    def __search_in_test_topics(self) -> QuerySet | None:
        return Test.objects.filter(topic__icontains=self.__request)

    def __search_in_test_texts(self) -> QuerySet | None:
        searching_results = []
        tests = Test.objects.all()
        for test in tests:
            test_json_str = json.dumps(test.test_json, ensure_ascii=False).encode('utf8')
            if self.__request.lower() in test_json_str.decode().lower():
                searching_results.append(test)
        return searching_results

    def __search_in_tests(self) -> Set:
        return set(self.__search_in_test_topics()) | set(self.__search_in_test_texts())

    def __search_in_media(self) -> Set:
        return set(Media.objects.filter(header__icontains=self.__request))
