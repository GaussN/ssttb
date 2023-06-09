import json

from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import get_object_or_404, redirect

from main.models import Progress
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

    def get_context_data(self, pk: int, **kwargs):
        context = super().get_context_data(**kwargs)

        test = get_object_or_404(Test, pk=pk)
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

    def post(self, request, pk, *args, **kwargs):
        if request.user.is_superuser:
            return self.render_to_response(self.get_context_data(**kwargs))
        request_body = json.loads(request.body)
        score = request_body['score']
        user_answers = request_body['answers']
        test = Test.objects.get(pk=pk)
        new_progress = Progress(user=request.user, test=test, score=score, user_answers=user_answers)
        new_progress.save()
        return redirect('result_page', pk=new_progress.pk)


class MediaListView(TemplateView):
    template_name = 'education/media_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media'] = Media.objects.filter(media_type=self.request.GET.get('media', 'VIDEO'))
        context['active_page'] = 'p_media'
        return context


class MediaView(DetailView):
    template_name = 'education/media.html'
    model = Media
    context_object_name = 'media'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'p_media'
        return context