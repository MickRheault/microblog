from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'creation_date')

admin.site.register(Tag, TagAdmin)

