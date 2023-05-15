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


class Media(models.Model):
    media_type = models.CharField(max_length=6, choices=(
        ('VIDEO', 'VIDEO'),
        ('SLIDES', 'SLIDES')
    ), verbose_name='Тип медиа')
    header = models.CharField(max_length=300, unique=True, verbose_name='Заголовок')
    describe = models.TextField(max_length=5000, verbose_name='Описание')
    url = models.URLField(verbose_name='Ссылка')

    def get_absolute_url(self):
        return reverse_lazy("media_page", args=[self.pk])

    class Meta:
        verbose_name = "Медиа"
        verbose_name_plural = 'Медиа'
