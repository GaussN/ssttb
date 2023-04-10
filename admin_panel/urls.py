from django.contrib.auth.models import User
from django.urls import path

import admin_panel.views as views
from education.models import Test, Lesson, Exercise


urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('test/<int:id>/', views.test_view, name="test_edit"),
    path('lesson/<int:id>/', views.test_view, name="lesson_edit"),
    path('exercise/<int:id>/', views.test_view, name="exercise_edit"),
    path('test/', views.records_list, kwargs={'model': Test, 'queryset': Test.objects.all()}, name="tests"),
    path('lesson/', views.records_list, kwargs={'model': Lesson, 'queryset': Lesson.objects.all()}, name="lessons"),
    path('exercise/', views.records_list, kwargs={'model': Exercise, 'queryset': Exercise.objects.all()}, name="exercises"),
    path('user/', views.records_list, kwargs={'model': User, 'queryset': User.objects.all()}, name="users"),
]

