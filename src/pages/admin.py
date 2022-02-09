from bs4 import BeautifulSoup
from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from django_seo_module.admin import DjangoSeoAdmin
from pages.model import Pages, PagesTwo


@admin.register(Pages)
class PagesAdmin(DjangoSeoAdmin):
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


@admin.register(PagesTwo)
class PagesAdmin(DjangoSeoAdmin):
    # print(super().list_display)
    list_display = ('colored_name',)
    fieldsets = (
        ('Likely Snippet ', {
            'fields': ('Google',)
        }),
        ('Page Meta (For only SEO Master)', {
            'classes': ('collapse', 'google_snippet'),
            # 'classes': ('google_snippet',),
            'fields': (
                'title',
                'slug',
                'description',
                'keywords',
                'index'
            ),
        }),
        ('Content page', {
            'fields': ('text_1',)
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
        # h1 = BeautifulSoup(self.text_1, features="html.parser").h1
        # return h1.text if h1 else f'{self.id=}'
        return obj.__str__()


    readonly_fields = ('Google',)
