import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from education.models import Test


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
