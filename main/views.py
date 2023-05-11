from math import ceil

from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import redirect

from education.models import Progress, Test
from .forms import RegisterUserForm, LoginUserForm
from utils.search import SearchUtil
from .models import *


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'home'
        if self.request.user.is_superuser:
           return context

        context['progress_percent'] = 0
        if Test.objects.count():
            context['progress_percent'] = \
                ceil(
                    Progress.objects.filter(user_id=8).values('test_id').distinct().count()
                    / Test.objects.count()
                    * 100
                )
        return context


class MediaListView(TemplateView):
    template_name = 'main/media_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media'] = Media.objects.filter(media_type=self.request.GET.get('media', 'VIDEO'))
        context['active_page'] = 'p_media'
        return context


class MediaView(DetailView):
    template_name = 'main/media.html'
    model = Media
    context_object_name = 'media'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'p_media'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'about'
        return context


class SearchView(TemplateView):
    template_name = 'app/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        q = request.GET.get('q', )
        if q:
            searcher = SearchUtil(request.GET['q'])
            context['search_result'] = searcher.search()
        return self.render_to_response(context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/forms/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'logup'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_page')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/forms/login.html'

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home_page'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'login'
        return context


def logout_user(request):
    logout(request)
    return redirect('home_page')


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['progress'] = Progress.objects.filter(user=self.request.user.pk)
        context['progress'] = Progress.objects.raw(
            "SELECT *, MAX(date) FROM education_progress GROUP BY test_id ORDER BY date ASC"
        )
        context['active_page'] = 'user_panel'
        return context

    def get(self, request, **kwargs):
        if request.user.is_superuser:
            return HttpResponse('''
            <h3><a href="/">Выход!</a></h3>
            <h1>Админам сюда нельзя</h1>
            <img src="https://static.rustore.ru/apk/1366735807/content/ICON/6a0cf744-3639-4b38-be33-0359289f252c.png">
            ''')
        return self.render_to_response(self.get_context_data(**kwargs))


class TestResultView(LoginRequiredMixin, TemplateView):
    template_name = "main/result.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['progress'] = Progress.objects.get(pk=pk)
        context['number_correct_answers_in_test'] = 0
        for question in context['progress'].test.test_json:
            for answer in question['answers']:
                if answer['right']:
                    context['number_correct_answers_in_test'] += 1
        return context

    def get(self, request, **kwargs):
        if request.user.is_superuser:
            return HttpResponse('''
            <h3><a href="/">Выход!</a></h3>
            <h1>Админам сюда нельзя</h1>
            <img src="https://static.rustore.ru/apk/1366735807/content/ICON/6a0cf744-3639-4b38-be33-0359289f252c.png">
            ''')
        return self.render_to_response(self.get_context_data(**kwargs))
