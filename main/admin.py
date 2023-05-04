from django.contrib import admin

from main.models import *


class MediaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'media_type', 'header', 'url')


admin.site.register(Media, MediaAdmin)
