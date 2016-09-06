from django.contrib import admin
from django.utils import timezone

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date',)

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['publish'] is True:
            obj.publish_date = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(Article, ArticleAdmin)
