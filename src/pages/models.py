from django_snippets.models import SnippetModel, models


class Pages(SnippetModel):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(
        max_length=120, help_text='max 120 characters', blank=True
    )
    description = models.TextField(
        max_length=120, help_text='max 120 characters', blank=True
    )

    def __str__(self):
        return str(self.id)
