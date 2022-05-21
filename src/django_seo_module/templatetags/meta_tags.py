from django import template
from pydantic import BaseModel, PyObject
from django.conf import settings


class PageModel(BaseModel):
    model: PyObject = settings.PAGE_MODEL


register = template.Library()


@register.inclusion_tag('meta_tags.html')
def meta(_id):
    return {'seo_model': PageModel().model.objects.get(id=_id)}
