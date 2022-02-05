from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class SnippetsAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("django_snippets.css", "admin/height_fields.css")
        }
        js = ("django_snippets.js",)
