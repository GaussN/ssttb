from django.db import models
from django.urls import reverse_lazy


class Media(models.Model):
    media_type = models.CharField(max_length=6, choices=(
        ('VIDEO', 'VIDEO'),
        ('SLIDES', 'SLIDES')
    ))
    header = models.CharField(max_length=300, unique=True)
    describe = models.TextField(max_length=5000)
    url = models.URLField()

    def get_absolute_url(self):
        return reverse_lazy("media_page", args=[self.pk])

    class Meta:
        verbose_name = "Медиа"
        verbose_name_plural = 'Медиа'
