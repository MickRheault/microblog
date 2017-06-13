from django import template
from re import sub

register = template.Library()


@register.filter(name="wrap_img")
def markdownify(content):
    pattern = r'(<img.*src="(.*)".*/>)'
    to = r'<a href="\2" class="pic">\1</a>'

    return sub(pattern, to, content)
