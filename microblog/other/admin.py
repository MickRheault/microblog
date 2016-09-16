from django.contrib import admin
from django.utils.text import slugify

from .models import Other


class OtherAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date',)
    fields = ('title', 'text', 'image')

    def save_model(self, request, obj, form, change):
        obj.author = request.user

        # Slugify title and save it as slug
        obj.slug = slugify(form.cleaned_data['title'], allow_unicode=True)

        super().save_model(request, obj, form, change)

admin.site.register(Other, OtherAdmin)
