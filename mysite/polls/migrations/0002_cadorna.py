# Generated by Django 4.2.7 on 2025-01-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cadorna",
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
                ("question_text", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
            ],
        ),
    ]
