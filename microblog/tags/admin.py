from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'creation_date')
    fields = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user

        super().save_model(request, obj, form, change)

admin.site.register(Tag, TagAdmin)

