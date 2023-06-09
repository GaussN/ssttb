from django.http import HttpResponse
from django.urls import path

import admin_panel.views as views

urlpatterns = [
    path('', views.AdminHome.as_view(), name="admin_home"),
    path('<str:app>/<str:model>/', views.RecordsListView.as_view(), name="records_list"),
    path('<str:app>/<str:model>/add/', views.AddRecordView.as_view(), name="add_page"),
    path('<str:app>/<str:model>/<int:pk>/', views.RecordView.as_view(), name="change_page"),
    path('<str:app>/<str:model>/<int:pk>/delete/', views.DeleteRecordView.as_view(), name="delete_page"),
]

