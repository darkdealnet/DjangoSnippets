from django.contrib import admin


class DjangoSeoAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("django_seo_module.css", "admin/height_fields.css")
        }
        js = ("django_seo_module.js",)
