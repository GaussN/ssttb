from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import *


def lessons_list(request: HttpRequest):
    lessons = Lesson.objects.filter(visible=True).order_by('num')
    return render(request, 'education/lessons.html', { 'active_page': 'lessons', 'lessons': lessons})


def tests_list(request: HttpRequest):
    tests = Test.objects.filter(visible=True)
    return render(request, 'education/tests.html', { 'active_page': 'lessons', 'tests': tests})


def exercises_list(request: HttpRequest):
    return render(request, 'education/exercises.html', { 'active_page': 'lessons'})


def lesson(request: HttpRequest, id: int):
    lesson = get_object_or_404(Lesson, num=id)
    topic = lesson.topic
    content = lesson.page
    
    next_lesson = None
    prev_lesson = None
    try: next_lesson = Lesson.objects.filter(num__gt=id, visible=True).first()
    except:  pass
    try: prev_lesson = Lesson.objects.filter(num__lt=id, visible=True).last()
    except: pass

    return render(request, 'education/lesson_base.html', { 
        'active_page': 'lessons', 
        'content': content, 
        'topic': topic, 
        'next_lesson': next_lesson,
        'prev_lesson': prev_lesson,
    })


def test(request: HttpRequest, id: int):
    test = get_object_or_404(Test, pk=id)
    topic = test.topic
    test_json = test.test_json

    from random import shuffle
    shuffle(test_json)
    for answers in test_json:
        shuffle(answers.get('answers'))

    return render(request, 'education/test_base.html', { 
        'active_page': 'lessons', 
        'questions': test_json, 
        'topic': topic, 
    })