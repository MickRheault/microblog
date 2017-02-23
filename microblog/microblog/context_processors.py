from core.models import Navigation

from .settings import META, INSTALLED_APPS


def meta(request):
    return META


def settings(request):
    return {
        'installed_apps': INSTALLED_APPS
    }


def navigation(request):
    nav_list = Navigation.objects.all().order_by('ordering')

    return {'nav_list': nav_list}
