# Generated by Django 5.1.1 on 2024-11-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PlumbingTemp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plumbing",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="Plumbing/"),
        ),
        migrations.AlterField(
            model_name="plumbing",
            name="link",
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
