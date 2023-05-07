from django.contrib import admin

from education.models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ('num', 'topic', 'page', 'visible', )
    list_filter = ('visible', )
    search_fields = ('num', 'topic',)
    ordering = ('num', )


class TestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'topic', 'visible')
    list_filter = ('visible', )
    search_fields = ('pk', 'topic',)
    ordering = ('pk', 'topic', )


class ProgressAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_id', 'test_id', 'date', 'score')
    list_filter = ('date', 'user_id', 'test_id')
    ordering = ('pk', 'score', 'date')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Progress, ProgressAdmin)
