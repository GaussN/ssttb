from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import *


class LessonsList(ListView):
    model = Lesson
    queryset = Lesson.objects.filter(visible=True)
    template_name = 'education/lessons.html'
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'lessons'
        return context


class TestsList(ListView):
    model = Test
    queryset = Test.objects.filter(visible=True)
    template_name = 'education/tests.html'
    context_object_name = 'tests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'tests'
        return context


class LessonView(TemplateView):
    template_name = 'education/lesson_base.html'

    def get_context_data(self, id: int, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = get_object_or_404(Lesson, num=id)
        next_lesson = None
        prev_lesson = None
        try:
            next_lesson = Lesson.objects.filter(num__gt=id, visible=True).first()
        except:
            pass
        try:
            prev_lesson = Lesson.objects.filter(num__lt=id, visible=True).last()
        except:
            pass

        context.update({
            'active_page': 'lessons',
            'lesson': lesson,
            'next_lesson': next_lesson,
            'prev_lesson': prev_lesson,
        })
        return context


class TestView(TemplateView):
    template_name = 'education/test_base.html'

    def get_context_data(self, id: int, **kwargs):
        context = super().get_context_data(**kwargs)

        test = get_object_or_404(Test, pk=id)
        test_json = test.test_json
        from random import shuffle
        shuffle(test_json)
        for answers in test_json:
            shuffle(answers.get('answers'))

        context.update({
            'active_page': 'tests',
            'test': test,
            'questions': test_json,
        })
        return context
