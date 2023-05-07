from django.db import models
from django.urls import reverse_lazy


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
