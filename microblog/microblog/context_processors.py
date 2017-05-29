from core.models import Navigation, SiteMeta, Footer

from .settings import INSTALLED_APPS


def settings(request):
    return {
        'installed_apps': INSTALLED_APPS
    }


def navigation(request):
    nav_list = Navigation.objects.all().order_by('ordering')

    return {'nav_list': nav_list}


def site_meta(request):
    obj = SiteMeta.get_solo()

    return {'site_meta': obj}


def footer(request):
    obj = Footer.get_solo()

    return  {'footer': obj}