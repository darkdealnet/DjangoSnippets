from django.utils.html import format_html
from django_seo_module.models import SeoModel, models
from tinymce.models import HTMLField

from django.contrib import admin


class Pages(SeoModel):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    header = models.CharField(
        max_length=80, help_text='max 80 characters',
        blank=True
    )
    text_1 = HTMLField(blank=True)


