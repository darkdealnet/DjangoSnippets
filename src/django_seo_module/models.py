from django.db import models
from django.utils.html import escape


class SeoModel(models.Model):
    title = models.CharField(
        max_length=80, help_text='max 80 characters',
        blank=True
    )
    description = models.TextField(
        max_length=160, help_text='max 160 characters',
        blank=True
    )
    keywords = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, help_text='For URL Page')
    index = models.BooleanField(
        default=True,
        help_text=escape(
            'if false add <meta name="robots" content="noindex">'
        )
    )
