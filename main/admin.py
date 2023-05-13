from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import *


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'media_type', 'header', 'url')


admin.site.register(Media, MediaAdmin)

UserAdmin.list_display = ('username', 'first_name', 'last_name', 'email', 'is_superuser')
