from django.urls import path

import main.views as views


urlpatterns = [
    path('', views.home, name='home_page'),
    path('literature/', views.literature_list, name='literature_list_page'),
    path('about/', views.about, name='about_page'),
]