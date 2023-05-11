import django.apps
from django.contrib import admin

from main.models import *


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'media_type', 'header', 'url')


admin.site.register(Media, MediaAdmin)
