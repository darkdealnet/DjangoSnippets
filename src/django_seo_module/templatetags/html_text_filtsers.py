from django import template
from django.utils.safestring import SafeString, mark_safe
from bs4 import BeautifulSoup as BS

register = template.Library()


@register.filter(name='first_tag')
def first_tag(html, tag_name):
    soup = BS(html, "html.parser")
    return getattr(soup, tag_name)


