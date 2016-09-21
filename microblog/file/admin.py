from django.contrib import admin

from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'extension', 'file_url', 'creation_date', 'author')
    fields = ('title', 'file')

    def file_url(self, obj):
        return obj.file_url

    file_url.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(File, FileAdmin)