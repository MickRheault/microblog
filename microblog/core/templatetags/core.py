from django import template
from django.conf import settings
from re import sub

register = template.Library()


@register.simple_tag
def version():
    return settings.VERSION

@register.filter(name="center_img")
def img(content):
    pattern = r'<img.*src="(.*)".*/>'
    to = r'<img src="\1" class="img-responsive center-block">'

    return sub(pattern, to, content)