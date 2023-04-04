from django.db import models


class Lesson(models.Model):
    num = models.PositiveIntegerField(unique=False, null=True, default=None)
    topic = models.CharField(max_length=150, unique=True)
    page = models.TextField()
    visible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f'/lesson/{self.num}'
    
    class Meta:
        verbose_name = 'Темы учебного материала'
        verbose_name_plural = 'Темы учебного материала'


class Test(models.Model):
    topic = models.CharField(max_length=150, unique=True)
    test_json = models.JSONField()
    visible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f'/test/{self.pk}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'