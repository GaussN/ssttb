from django.urls import path

import education.views as views


urlpatterns = [ 
    path('lessons/', views.LessonsList.as_view(), name='lessons_list_page'),
    path('lesson/<int:id>', views.LessonView.as_view(), name='lesson_page'),
    path('tests/', views.TestsList.as_view(), name='tests_list_page'),
    path('test/<int:pk>', views.TestView.as_view(), name='test_page'),
    path('media/', views.MediaListView.as_view(), name='all_media_page'),
    path('media/<int:pk>', views.MediaView.as_view(), name='media_page'),
]
