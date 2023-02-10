# Generated by Django 3.2.16 on 2023-02-10 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0002_auto_20230207_1242"),
    ]

    operations = [
        migrations.RenameField(
            model_name="group",
            old_name="text",
            new_name="description",
        ),
        migrations.AlterField(
            model_name="follow",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddConstraint(
            model_name="follow",
            constraint=models.UniqueConstraint(
                fields=("user", "following"), name="unique_follow"
            ),
        ),
    ]
