from django import template
from pydantic import BaseModel, PyObject


class PageModel(BaseModel):
    model: PyObject = 'pages.models.Pages'


register = template.Library()


@register.inclusion_tag('meta_tags.html')
def meta(_id):
    return {'seo_model': PageModel().model.objects.get(id=_id)}
