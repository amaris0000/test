# Generated by Django 4.2.13 on 2024-05-15 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0003_hashtag_content_tags"),
        ("users", "0003_favoritetag"),
    ]

    operations = [
        migrations.CreateModel(
            name="FavoriteContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contents.content",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
