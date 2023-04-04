from django.urls import path

import main.views as views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('literature/', views.LiteratureListView.as_view(), name='literature_list_page'),
    path('about/', views.AboutView.as_view(), name='about_page'),
]