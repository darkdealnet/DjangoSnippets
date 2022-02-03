from django_snippets.models import SnippetModel, models
from tinymce.models import HTMLField


class Pages(SnippetModel):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(
        max_length=80, help_text='max 80 characters', blank=True
    )
    description = models.TextField(
        max_length=160, help_text='max 160 characters', blank=True
    )

    text_1 = HTMLField(blank=True)
