from django.contrib import admin

from .models import Navigation, Footer, SiteMeta

from solo.admin import SingletonModelAdmin

admin.site.register(Navigation)
admin.site.register(Footer, SingletonModelAdmin)
admin.site.register(SiteMeta, SingletonModelAdmin)