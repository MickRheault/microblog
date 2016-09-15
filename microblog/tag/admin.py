from slugify import slugify

from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'creation_date')
    fields = ('title',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user

        # Slugify title and save it as slug
        obj.slug = slugify(form.cleaned_data['title'])

        super().save_model(request, obj, form, change)

admin.site.register(Tag, TagAdmin)

