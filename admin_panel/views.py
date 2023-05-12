from django.contrib import admin
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import Http404, HttpResponse, HttpRequest
from django.apps import apps

from admin_panel.mixins import SuperuserTestMixin
from education.models import *
from .forms import *


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

    def get_context_data(self, model, **kwargs):
        admin_model = admin.site._registry.get(model, )
        if not admin_model:
            raise Http404()

        context = super().get_context_data(**kwargs)
        context['list_display'] = admin_model.list_display
        context['objects'] = model.objects.all()
        context['meta'] = model._meta
        return context

    def get(self, request, app, model: str, **kwargs):
        try:
            model = apps.get_model(app, model)
        except (LookupError, ValueError, TypeError):
            raise Http404
        context = self.get_context_data(model, **kwargs)
        return self.render_to_response(context)


class RecordView(SuperuserTestMixin, TemplateView):
    def get_context_data(self, app, model, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        model = apps.get_model(app, model)
        if not model:
            raise Http404()
        context['object'] = model.objects.get(pk=pk)
        context['meta'] = model._meta
        context['form'] = forms_relation.get(model, modelform_factory(model, fields='__all__'))(instance=context['object'])
        return context

    def get(self, request: HttpRequest, app: str, model: str, pk: int, **kwargs):
        template_name = f'admin_panel/{model}.html'
        context = self.get_context_data(app, model, pk, **kwargs)
        return render(request, template_name, context)

    def post(self, request, app, model, pk, **kwargs):
        return HttpResponse('KURWA')
