from django import forms

from education.models import Lesson, Test
from main.models import Media


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('num', 'topic', 'page', 'visible')


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('topic', 'test_json', 'visible')


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ('media_type', 'header', 'describe', 'url')


forms_relation = {
    Lesson: LessonForm,
    Test: TestForm,
    Media: MediaForm,
}
