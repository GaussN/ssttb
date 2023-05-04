from django.urls import path

import education.views as views


urlpatterns = [ 
    path('lessons/', views.LessonsList.as_view(), name='lessons_list_page'),
    path('lesson/<int:id>', views.LessonView.as_view(), name='lesson_page'),
    path('tests/', views.TestsList.as_view(), name='tests_list_page'),
    path('test/<int:id>', views.TestView.as_view(), name='test_page'),
]