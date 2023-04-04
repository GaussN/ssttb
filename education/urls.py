from django.urls import path

import education.views as views


urlpatterns = [ 
    path('lessons/', views.lessons_list, name='lessons_list_page'),
    path('lesson/<int:id>', views.lesson, name='lesson_page'),
    path('tests/', views.tests_list, name='tests_list_page'),
    path('test/<int:id>', views.test, name='test_page'),
    path('exercises/', views.exercises_list, name='exercises_list_page'),
]