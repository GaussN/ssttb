import datetime

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import models


class Lesson(models.Model):
    num = models.PositiveIntegerField(unique=False, null=True, default=None)
    topic = models.CharField(max_length=150, unique=True)
    page = models.TextField()
    visible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse_lazy("lesson_page", args=[self.num])

    class Meta:
        verbose_name = 'Темы учебного материала'
        verbose_name_plural = 'Темы учебного материала'


class Test(models.Model):
    topic = models.CharField(max_length=150, unique=True)
    test_json = models.JSONField()
    visible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse_lazy("test_page", args=[self.pk])

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now, auto_created=True, editable=False)
    score = models.IntegerField()
    user_answers = models.JSONField()

    def get_absolute_utl(self):
        return reverse_lazy("result_page", args=[self.pk])

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'
