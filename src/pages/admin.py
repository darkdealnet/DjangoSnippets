import json

from bs4 import BeautifulSoup
from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from django_seo_module.admin import DjangoSeoAdmin
from pages.models import Pages, PagesTwo, PagesSlug, PagesManyText, \
    PageCKeditor


@admin.register(Pages)
class PagesAdmin(DjangoSeoAdmin):
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
            'text_field': 'text_1',
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
class PagesTwoAdmin(DjangoSeoAdmin):
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
                'auto_compile_title',
                'description',
                'auto_compile_description',
                'keywords',
                'index'
            ),
        }),
        ('Content page', {
            'fields': ('text_1',)
        }),
    )

    def Google(self, obj):
        context = {
            'class': 'auto-snippet',
            'settings': json.dumps({
                'idTitle': 'id_title',
                'idDescription': 'id_description',
                'textFields': ['id_text_1', 'id_text_2'],
                'slug': False,
            })
        }
        return render_to_string('google.html', context)

    @admin.display
    def colored_name(self, obj):
        # h1 = BeautifulSoup(self.text_1, features="html.parser").h1
        # return h1.text if h1 else f'{self.id=}'
        return obj.__str__()

    readonly_fields = ('Google',)


@admin.register(PagesSlug)
class PagesSlugAdmin(DjangoSeoAdmin):
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
                'auto_compile_title',
                'description',
                'auto_compile_description',
                'keywords',
                'index'
            ),
        }),
        ('Content page', {
            'fields': ('slug', 'text_1',)
        }),
    )

    def Google(self, obj):
        context = {
            'class': 'auto-snippet',
            'settings': json.dumps({
                'idTitle': 'id_title',
                'idDescription': 'id_description',
                'textFields': ['id_text_1'],
                'slug': True,
            })
        }
        return render_to_string('google.html', context)

    @admin.display
    def colored_name(self, obj):
        # h1 = BeautifulSoup(self.text_1, features="html.parser").h1
        # return h1.text if h1 else f'{self.id=}'
        return obj.__str__()

    readonly_fields = ('Google',)


@admin.register(PagesManyText)
class PagesManyTextAdmin(DjangoSeoAdmin):
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
                'auto_compile_title',
                'description',
                'auto_compile_description',
                'keywords',
                'index'
            ),
        }),
        ('Content page', {
            'fields': ('slug', 'text_1', 'text_2')
        }),
    )

    def Google(self, obj):
        context = {
            'class': 'auto-snippet',
            'settings': json.dumps({
                'idTitle': 'id_title',
                'idDescription': 'id_description',
                'textFields': ['id_text_1', 'id_text_2'],
                'slug': True,
            })
        }
        return render_to_string('google.html', context)

    @admin.display
    def colored_name(self, obj):
        # h1 = BeautifulSoup(self.text_1, features="html.parser").h1
        # return h1.text if h1 else f'{self.id=}'
        return obj.__str__()

    readonly_fields = ('Google',)


@admin.register(PageCKeditor)
class PagesManyTextAdmin(DjangoSeoAdmin):
    list_display = ('colored_name',)
    fieldsets = (
        ('Likely Snippet ', {
            'fields': ('google',)
        }),
        ('Page Meta (For only SEO Master)', {
            'classes': ('collapse', 'google_snippet'),
            # 'classes': ('google_snippet',),
            'fields': (
                'title',
                'auto_compile_title',
                'description',
                'auto_compile_description',
                'keywords',
                'index'
            ),
        }),
        ('Content page', {
            'fields': ('slug', 'content')
        }),
    )

    def google(self, obj):
        context = {
            'class': 'auto-snippet',
            'settings': json.dumps({
                'idTitle': 'id_title',
                'idDescription': 'id_description',
                'textFields': ['id_content'],
                'slug': True,
            })
        }
        return render_to_string('google.html', context)

    @admin.display
    def colored_name(self, obj):
        # h1 = BeautifulSoup(self.text_1, features="html.parser").h1
        # return h1.text if h1 else f'{self.id=}'
        return obj.__str__()

    readonly_fields = ('google',)
