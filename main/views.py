from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import *


def home(request: HttpRequest):
    return render(request, 'main/home.html', { 'active_page': 'home' })


def literature_list(request: HttpRequest):
    return render(request, 'main/literature.html', { 'active_page': 'literature', 'books': Book.objects.all()})


def about(request: HttpRequest):
    return render(request, 'main/about.html', { 'active_page': 'about' })
