# Generated by Django 4.2.7 on 2025-01-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_pic"),
    ]

    operations = [
        migrations.AddField(
            model_name="ad",
            name="content_type",
            field=models.CharField(
                blank=True,
                help_text="The MIMEType of the file",
                max_length=256,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="picture",
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
