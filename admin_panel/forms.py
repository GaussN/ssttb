from django import forms
from django.contrib.auth.models import User

from education.models import Lesson, Test
from main.models import Media


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


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('topic', 'test_json', 'visible')


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
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }


forms_relation = {
    Lesson: LessonForm,
    Test: TestForm,
    Media: MediaForm,
    User: UserForm
}
