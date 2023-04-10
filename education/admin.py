from django.contrib import admin

from education.models import *


class LessonAdmin(admin.ModelAdmin):
    @admin.action(description="Увеличить значения num")
    def increment(modelamdin, request, queryset):
        queryset = queryset.order_by('-num')
        for i in queryset:
            try:
                i.num += 1
                i.save()
            except:
                print('unique constraint')

    @admin.action(description="Уменьшить значения num")
    def decrement(modelamdin, request, queryset):
        queryset = queryset.order_by('-num')
        for i in queryset:
            try:
                i.num -= 1
                i.save()
            except:
                print('unique constraint')

    list_display = ('num', 'topic', 'page', 'visible', )
    list_filter = ('visible', )
    search_fields = ('num', 'topic',)
    ordering = ('num', )
    actions = (increment, decrement, )


class TestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'topic', 'visible')
    list_filter = ('visible', )
    search_fields = ('pk', 'topic',)
    ordering = ('pk', 'topic', )


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'exercise', 'visible')
    list_filter = ('visible', )
    search_fields = ('pk', 'topic',)
    ordering = ('pk',)


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Exercise, ExerciseAdmin)