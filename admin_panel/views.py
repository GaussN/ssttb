import json

from django.contrib import admin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from django.apps import apps
from django.db import utils

from admin_panel.mixins import SuperuserTestMixin
from education.models import *
from main.models import *


class AdminHome(SuperuserTestMixin, TemplateView):
    template_name = 'admin_panel/admin_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = [
            {'meta': Test._meta, 'objects': Test.objects, },
            {'meta': Lesson._meta, 'objects': Lesson.objects, },
            {'meta': Media._meta, 'objects': Media.objects, },
            {'meta': User._meta, 'objects': User.objects, },
        ]
        return context


class RecordsListView(SuperuserTestMixin, TemplateView):
    template_name = 'admin_panel/records_list.html'

    def get(self, request, app_model, **kwargs):
        model = None
        try:
            model = apps.get_model(*app_model.split('/'))
        except (LookupError, ValueError, TypeError):
            raise Http404()
        admin_model = admin.site._registry.get(model)

        context = super().get_context_data(**kwargs)

        context['list_display'] = admin_model.list_display
        context['objects'] = model.objects.all()
        context['meta'] = model._meta
        return self.render_to_response(context)



@login_required
@user_passes_test(lambda user: user.is_superuser)
def records_list(request: HttpRequest, **kwargs):
    return render(request, 'admin_panel/records_list.html', kwargs)


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
