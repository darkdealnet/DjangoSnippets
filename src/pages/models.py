from django.urls import reverse
from django.utils.html import format_html
from django_seo_module.models import SeoModel, models
from tinymce.models import HTMLField
from bs4 import BeautifulSoup


class Pages(SeoModel):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    header = models.CharField(
        max_length=80, help_text='max 80 characters',
        blank=True
    )
    text_1 = HTMLField(blank=True)

    def __str__(self):
        return self.header


class PagesTwo(SeoModel):
    class Meta:
        verbose_name = 'PageTwo'
        verbose_name_plural = 'PagesTwo'

    text_1 = HTMLField(blank=True)
    slug = None

    def __str__(self):
        first = BeautifulSoup(self.text_1, features="html.parser").find()
        if first:
            return first.text if first.name == 'h1' else f'ERROR: first tag not "h1"'
        else:
            return 'content not found'

    def get_absolute_url(self):
        return reverse('pageTwo', kwargs={'page_id': self.id})
