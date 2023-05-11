from django.http import HttpResponse
from django.urls import path

import admin_panel.views as views

urlpatterns = [
    path('', views.AdminHome.as_view(), name="admin_home"),
    path('<str:app>/<str:model>/', views.RecordsListView.as_view(), name="records_list"),
    path('<str:app>/<str:model>/add/', lambda request, app, model, : HttpResponse('NEW GENA'), name="add_page"),
    path('<str:app>/<str:model>/<int:pk>/', views.RecordView.as_view(), name="change_page"),
    path('<str:app>/<str:model>/<int:pk>/delete/', lambda request, app, model, pk: HttpResponse(f'RIP {pk} GENA'), name="delete_page"),
]

