from django import template
from django_snippets.models import SnippetModel

register = template.Library()


@register.inclusion_tag('meta_tags.html')
def meta(_id):
    return {'seo_model': SnippetModel.objects.get(id=_id)}

