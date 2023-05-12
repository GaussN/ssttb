import datetime
import json

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import models


class Lesson(models.Model):
    num = models.PositiveIntegerField(unique=False, null=True, default=None, verbose_name='Порядковый номер')
    topic = models.CharField(max_length=150, unique=True, verbose_name='Тема')
    page = models.TextField(verbose_name='Код страницы')
    visible = models.BooleanField(default=True, verbose_name='Видимость')

    def get_absolute_url(self):
        return reverse_lazy("lesson_page", args=[self.num])

    def update(self, post):
        self.num = post.get('num', self.num)
        self.topic = post.get('topic', self.topic)
        self.page = post.get('page', self.page)
        self.visible = post.get('visible') == 'on' or self.visible

    class Meta:
        verbose_name = 'Темы учебного материала'
        verbose_name_plural = 'Темы учебного материала'


class Test(models.Model):
    topic = models.CharField(max_length=150, unique=True, verbose_name='Тема')
    test_json = models.JSONField(verbose_name="Вопросы с ответами(JSON)")
    visible = models.BooleanField(default=True, verbose_name='Видимость')

    def get_absolute_url(self):
        return reverse_lazy("test_page", args=[self.pk])

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Идентификатор пользователя')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Идентификатор теста')
    date = models.DateTimeField(default=datetime.datetime.now, auto_created=True, editable=False,
                                verbose_name='Дата прохождения')
    score = models.IntegerField(verbose_name='Количество набранных баллов')
    user_answers = models.JSONField(verbose_name='Ответы пользователя(JSON)')

    def get_absolute_utl(self):
        return reverse_lazy("result_page", args=[self.pk])

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'
