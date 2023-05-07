import json

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db import utils

from education.admin import *
from education.models import *
from main.admin import MediaAdmin
from main.models import Media


class AdminHome(UserPassesTestMixin, TemplateView):
    template_name = 'admin_panel/admin_home.html'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('/login/?next=/admin/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = [
            {'meta': Test._meta, 'objects': Test.objects, 'admin_model': TestAdmin},
            {'meta': Lesson._meta, 'objects': Lesson.objects, 'admin_model': LessonAdmin},
            {'meta': Media._meta, 'objects': Media.objects, 'admin_model': MediaAdmin},
            {'meta': User._meta, 'objects': User.objects, 'admin_model': type('UserAdmin', (), {'list_display': ('username', 'login', 'email', 'is_superuser')})},
        ]
        return context


@login_required
@user_passes_test(lambda user: user.is_superuser)
def records_list(request: HttpRequest, **kwargs):
    return render(request, 'admin_panel/records_list.html', kwargs)


@login_required
@user_passes_test(lambda user: user.is_superuser)
def test_update(request: HttpRequest, id: int):
    return render(request, 'admin_panel/test.html', {'test': Test.objects.get()})


@login_required
@user_passes_test(lambda user: user.is_superuser)
def test_add(request: HttpRequest):
    if request.method == 'POST':
        post = json.loads(request.body)
        try:
            test = Test(
                topic=post.get('title'),
                test_json=post.get('questions'),
                visible=post.get('visible')
            )
            test.save()
        except utils.Error as er:
            print(f"{er=}")
        # возврат json с сообщением: "успех"/"не успех"
        return redirect(reverse_lazy('tests'))
    return render(request, 'admin_panel/test.html')
