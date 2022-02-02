from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class SnippetsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Likely Snippet ', {
            'fields': ('Google',)
        }),
        ('Page Meta', {
            'classes': ('wide', 'google_snippet'),
            'fields': ('probability', 'title', 'description',),
        }),
    )

    readonly_fields = (
        'probability',
        'Google'
    )

    @admin.display(empty_value='Нужно заполнить')
    def probability(self, obj):
        print(obj.title)
        return obj.title

    def Google(self, obj):
        return render_to_string('google.html')

    class Media:
        css = {
            "all": ("django_snippets.css",)
        }
        js = ("django_snippets.js",)
