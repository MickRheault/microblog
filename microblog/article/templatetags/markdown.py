from django import template
from markdown import markdown

from microblog.settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
)

register = template.Library()


@register.filter(name="markdownify")
def markdownify(content):
    md = markdown(
        text=content,
        extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
    )
    return md