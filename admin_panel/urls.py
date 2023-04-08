from django.urls import path

import admin_panel.views as views


urlpatterns = [
    path('test/<int:id>/update', views.test_view, name="test_edit"),
]