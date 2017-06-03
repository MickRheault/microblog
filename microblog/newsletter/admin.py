from django.contrib import admin
from django.db import models

from markdownx.widgets import AdminMarkdownxWidget
from solo.admin import SingletonModelAdmin

from .models import EmailBase, Raport, BannedEmailDomain, BannedEmail, SpecialOffer


class SpecialOfferAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


class RaportAdmin(SingletonModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


admin.site.register(EmailBase)
admin.site.register(Raport, RaportAdmin)
admin.site.register(BannedEmailDomain)
admin.site.register(BannedEmail)
admin.site.register(SpecialOffer, SpecialOfferAdmin)

