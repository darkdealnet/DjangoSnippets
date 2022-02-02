from django.contrib import admin
from django_snippets.admin import SnippetsAdmin
from pages.models import Pages


@admin.register(Pages)
class PagesAdmin(SnippetsAdmin):
    list_display = ('title',)

    # def custom_title(self):
    #     return self.title
    #
    # def show_preview(self, obj):
    #     if obj:
    #         return mark_safe('<span>123</span>')
