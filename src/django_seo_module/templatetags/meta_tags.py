from django import template

from pages.model import Pages

register = template.Library()


@register.inclusion_tag('meta_tags.html')
def meta(_id):
    return {'seo_model': Pages.objects.get(id=_id)}

