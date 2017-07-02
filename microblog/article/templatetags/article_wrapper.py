from django import template
from re import sub

register = template.Library()


@register.filter(name="wrap_img")
def markdownify(content):
    pattern = r'<img.*src="(.*)".*/>'
    to = r'<a href="\1" class="pic"><img src="\1" class="img-responsive center-block"/></a>'

    return sub(pattern, to, content)
