from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import RegisterUserForm, LoginUserForm
from .models import *
from .utils.search import SearchUtil


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'home'
        return context


class MediaListView(ListView):
    template_name = 'main/media_list.html'
    model = Media
    context_object_name = 'all_media'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'p_media'
        return context


class MediaView(TemplateView):
    template_name = 'main/media.html'
    model = Media
    context_object_name = 'media'

    def get_context_data(self, id: int, **kwargs):
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
        q = request.GET.get('q', '')
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
    template_name = "main/forms/login.html"

    def get_success_url(self):
        return reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'login'
        return context


def logout_user(request):
    logout(request)
    return redirect('home_page')
