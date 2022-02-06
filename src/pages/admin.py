from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from django_snippets.admin import SnippetsAdmin
from pages.model import Pages


@admin.register(Pages)
class PagesAdmin(SnippetsAdmin):
    # print(super().list_display)
    list_display = ('title', 'colored_name',)
    prepopulated_fields = {'slug': ('header',)}
    fieldsets = (
        ('Likely Snippet ', {
            'fields': ('Google',)
        }),
        ('Page Meta (For only SEO Master)', {
            # 'classes': ('collapse', 'google_snippet'),
            'classes': ('google_snippet',),
            'fields': (
                'title',
                'slug',
                'description',
                'keywords',
                'index'
            ),
        }),
        ('Content page', {
            'fields': ('header', 'text_1',)
        }),
    )

    def custom_title(self):
        return self.title

    def Google(self, obj):
        context = {
            'text_fields': 'text1, text2',
        }
        return render_to_string('google.html', context)

    @admin.display
    def colored_name(self, obj):
        return format_html(
            '<span style="color: #{};">123</span>',
            '871f1f',
        )

    readonly_fields = ('Google',)
