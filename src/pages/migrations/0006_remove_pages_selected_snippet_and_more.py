# Generated by Django 4.0 on 2022-02-18 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_pages_selected_snippet_pagestwo_selected_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='selected_snippet',
        ),
        migrations.RemoveField(
            model_name='pagestwo',
            name='selected_snippet',
        ),
    ]
