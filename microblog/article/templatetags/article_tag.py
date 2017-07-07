from django import template
from django.utils.safestring import mark_safe

from article.models import Article

register = template.Library()


@register.simple_tag
def generate_status_submit(id, form="status-form"):
    obj = Article.objects.get(pk=id)
    html_tag = '<input class="default inp-status" type="submit" form="{}" name="___{}" value="{}" />'
    l = [html_tag.format(form, o.name, list(filter(lambda s: s[0] == o.target, Article.STATUS_CHOICES))[0][1])
         for o in list(Article.get_available_status_transitions(obj))]

    return mark_safe(" ".join(l))




