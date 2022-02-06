from django import template
from django_seo_module.models import SeoModel

register = template.Library()


@register.inclusion_tag('meta_tags.html')
def meta(_id):
    return {'seo_model': SeoModel.objects.get(id=_id)}

