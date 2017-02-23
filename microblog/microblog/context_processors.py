from core.models import Navigation

from .settings import META


def meta(request):
    return META


def navigation(request):
    nav_list = Navigation.objects.all().order_by('ordering')

    return {'nav_list': nav_list}
