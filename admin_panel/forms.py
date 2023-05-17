import random

from bulk_update.helper import bulk_update
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms

from education.models import Lesson, Test, Media


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('num', 'topic', 'page', 'visible')
        widgets = {
            'num': forms.NumberInput(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'page': forms.Textarea(attrs={'class': 'form-control'}),
            'visible': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

    def clean_num(self):
        """
        Исключает повторы порядкового номера
        """
        num = self.cleaned_data['num']
        # if not Lesson.objects.filter(num=num).count():
        #     return num
        if self.instance and self.instance.num == num:
            return num
        lessons = Lesson.objects.filter(num__gte=num)
        for i, l in enumerate(lessons):
            l.num = i + num + 1
        bulk_update(lessons, update_fields=['num'])
        return num


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('topic', 'test_json', 'visible')

    def clean_topic(self):
        topic = self.cleaned_data['topic']
        if self.instance and self.instance.topic == topic:
            return topic

        topics = Test.objects.filter(topic=topic)
        if not topics.count():
            return topic
        return f"{topic}(W:Такая тема теста уже существует)" + chr(random.randint(97, 122))


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ('media_type', 'header', 'describe', 'url')
        widgets = {
            'media_type': forms.Select(attrs={'class': 'form-control'}),
            'header': forms.TextInput(attrs={'class': 'form-control'}),
            'describe': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_superuser')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        emails = User.objects.filter(email=email)
        if self.instance:
            emails = emails.exclude(pk=self.instance.pk)
        if emails.count():
            raise ValidationError('Почта уже используется')
        return email

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


forms_relation = {
    Lesson: LessonForm,
    Test: TestForm,
    Media: MediaForm,
    User: UserForm
}
