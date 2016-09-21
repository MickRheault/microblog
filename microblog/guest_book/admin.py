from django.contrib import admin
from django.forms import Textarea

from .models import GuessBookEntry


class GuessBookEntryAdmin(admin.ModelAdmin):
    fields = ('author', 'text')

    def formfield_for_dbfield(self, db_field, **kwargs):
        # Setup widget to specified field
        if db_field.name == 'text':
            kwargs['widget'] = Textarea

        return super(GuessBookEntryAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(GuessBookEntry, GuessBookEntryAdmin)
