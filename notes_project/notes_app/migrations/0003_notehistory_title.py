# Generated by Django 5.0.2 on 2024-02-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes_app", "0002_notehistory"),
    ]

    operations = [
        migrations.AddField(
            model_name="notehistory",
            name="title",
            field=models.CharField(default="previouslyEmptyTitle", max_length=200),
            preserve_default=False,
        ),
    ]
