from django.http import HttpResponse
from django.urls import path

import admin_panel.views as views

urlpatterns = [
    path('', views.AdminHome.as_view(), name="admin_home"),
    path('<path:app_model>/', views.RecordsListView.as_view(), name="records_list"),
    path('<path:app_model>/add', lambda request, app_model, : HttpResponse('NEW GENA'), name="add_page"),
    path('<path:app_model>/<int:id>', lambda request, app_model, id: HttpResponse(f'{id} GENA'), name="change_page"),
    path('<path:app_model>/<int:id>/delete', lambda request, app_model, id: HttpResponse(f'RIP {id} GENA'), name="delete_page"),
]

