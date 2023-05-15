from django.contrib import admin

from education.models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ('num', 'topic', 'page', 'visible', )
    list_filter = ('visible', )
    search_fields = ('num', 'topic',)
    ordering = ('num', )


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'visible')
    list_filter = ('visible', )
    search_fields = ('pk', 'topic',)
    ordering = ('id', 'topic', )


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'media_type', 'header', 'url')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Media, MediaAdmin)
