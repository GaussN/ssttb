from django.contrib import admin

from main.models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'link') 


admin.site.register(Book, BookAdmin)
