from django.contrib.auth.models import User
from django.urls import path

import admin_panel.views as views
from education.models import Test, Lesson


urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('test/<int:id>/', views.test_update, name="test_update"),
    path('test/add', views.test_add, name="test_add"),
    path('lesson/<int:id>/', views.test_update, name="lesson_edit"),
    path('test/', views.records_list, kwargs={'model': Test, 'queryset': Test.objects.all()}, name="tests"),
    path('lesson/', views.records_list, kwargs={'model': Lesson, 'queryset': Lesson.objects.all()}, name="lessons"),
    path('user/', views.records_list, kwargs={'model': User, 'queryset': User.objects.all()}, name="users"),
]

