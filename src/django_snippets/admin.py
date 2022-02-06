from django.contrib import admin

class SnippetsAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("django_snippets.css", "admin/height_fields.css")
        }
        js = ("django_snippets.js",)
