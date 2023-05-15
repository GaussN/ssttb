from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import *


class ProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'test_id', 'date', 'score')
    list_filter = ('date', 'user_id', 'test_id')
    ordering = ('id', 'score', 'date')


admin.site.register(Progress, ProgressAdmin)

UserAdmin.list_display = ('username', 'first_name', 'last_name', 'email', 'is_superuser')
