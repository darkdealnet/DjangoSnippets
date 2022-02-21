import os
from pathlib import Path

from django.contrib import admin

BASE_DIR = Path(__file__).resolve().parent


class DjangoSeoAdmin(admin.ModelAdmin):
    class Media:
        js = ['snippet/' + i for i in os.listdir(BASE_DIR / 'static/snippet')]
