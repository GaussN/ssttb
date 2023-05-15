from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest
from django.forms import modelform_factory
from django.contrib import admin
from django.apps import apps

from admin_panel.mixins import SuperuserTestMixin
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
        admin_model = admin.site._registry.get(model)
        if not admin_model:
            raise Http404()

        context = super().get_context_data(**kwargs)
        context['list_display'] = admin_model.list_display
        context['objects'] = model.objects.all()
        context['meta'] = model._meta
        return context

    def get(self, request, app, model: str, **kwargs):
        try:
            model_cls = apps.get_model(app, model)
        except (LookupError, ValueError, TypeError):
            raise Http404
        context = self.get_context_data(model_cls, **kwargs)
        return self.render_to_response(context)


class RecordView(SuperuserTestMixin, TemplateView):
    def get_context_data(self, app, model, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        model_cls = apps.get_model(app, model)
        if not model_cls:
            raise Http404()
        context['object'] = model_cls.objects.get(pk=pk)
        context['meta'] = model_cls._meta
        context['form'] = forms_relation.get(
            model_cls, modelform_factory(model_cls, fields='__all__')
        )(instance=context['object'])
        return context

    def get(self, request: HttpRequest, app: str, model: str, pk: int, **kwargs):
        # нет проверки на существование шаблона
        template_name = f'admin_panel/{model}.html'
        context = self.get_context_data(app, model, pk, **kwargs)
        return render(request, template_name, context)

    def post(self, request, app, model, pk, **kwargs):
        model_cls = apps.get_model(app, model)
        obj = model_cls.objects.get(pk=pk)
        form_cls = forms_relation.get(
            model_cls, modelform_factory(model_cls, fields='__all__')
        )

        form = form_cls(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('records_list', app=app, model=model, permanent=True)

        template_name = f'admin_panel/{model}.html'
        context = self.get_context_data(app, model, pk, **kwargs)
        context['form'] = form
        return render(request, template_name, context)


class AddRecordView(SuperuserTestMixin, TemplateView):
    def get_context_data(self, app, model, **kwargs):
        context = super().get_context_data(**kwargs)
        model_cls = apps.get_model(app, model)
        if not model_cls:
            raise Http404()
        context['meta'] = model_cls._meta
        context['form'] = forms_relation.get(
            model_cls, modelform_factory(model_cls, fields='__all__')
        )()
        return context

    def get(self, request, app, model, **kwargs):
        # нет проверки на существование шаблона
        template_name = f'admin_panel/{model}.html'
        context = self.get_context_data(app, model, **kwargs)
        return render(request, template_name, context)

    def post(self, request, app, model, **kwargs):
        model_cls = apps.get_model(app, model)
        form_cls = forms_relation.get(
            model_cls, modelform_factory(model_cls, fields='__all__')
        )

        form = form_cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records_list', app=app, model=model, permanent=True)

        template_name = f'admin_panel/{model}.html'
        context = self.get_context_data(app, model, **kwargs)
        context['form'] = form
        return render(request, template_name, context)


class DeleteRecordView(SuperuserTestMixin, TemplateView):
    template_name = 'admin_panel/delete.html'
    def get_context_data(self, app, model, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        model_cls = apps.get_model(app, model)
        if not model_cls:
            raise Http404()
        context['meta'] = model_cls._meta
        context['object'] = model_cls.objects.get(pk=pk)
        return context

    # def get(self, app, model, pk, **kwargs):
    #     model_cls =
    #     return redirect('records_list', app=app, model=model)

    def post(self, request, app, model, pk, **kwargs):
        model_cls = apps.get_model(app, model)
        obj = model_cls.objects.get(pk=pk)
        obj.delete()
        return redirect('records_list', app=app, model=model)
