# Generated by Django 5.1 on 2024-09-04 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"verbose_name": "блог", "verbose_name_plural": "блог"},
        ),
    ]
