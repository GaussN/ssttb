from django.urls import path

import main.views as views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('media/', views.MediaListView.as_view(), name='all_media_page'),
    path('media/<int:pk>', views.MediaView.as_view(), name='media_page'),
    path('about/', views.AboutView.as_view(), name='about_page'),
    path('logup/', views.RegisterUser.as_view(), name='reg_page'),
    path('login/', views.LoginUser.as_view(), name='auth_page'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('profile/', views.UserProfileView.as_view(), name='profile_page'),
]
