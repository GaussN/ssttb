from django.urls import path

import main.views as views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('literature/', views.LiteratureListView.as_view(), name='literature_list_page'),
    path('about/', views.AboutView.as_view(), name='about_page'),
    path('logup/', views.RegisterUser.as_view(), name='reg_page'),
    path('login/', views.AboutView.as_view(), name='auth_page'),
]
