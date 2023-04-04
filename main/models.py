from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=100)
    link = models.CharField(max_length=300, unique=True, null=True, default=None)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'