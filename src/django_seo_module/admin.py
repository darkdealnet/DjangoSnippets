from django.contrib import admin


class DjangoSeoAdmin(admin.ModelAdmin):
    class Media:
        js = (
            "snippet/131.bundle.js",
            "snippet/main.bundle.js"
        )
