# Generated by Django 4.2.13 on 2024-05-12 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="content",
            old_name="name",
            new_name="title",
        ),
    ]
