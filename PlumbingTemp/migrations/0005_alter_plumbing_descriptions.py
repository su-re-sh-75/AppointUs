# Generated by Django 5.1.1 on 2024-11-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PlumbingTemp", "0004_alter_plumbing_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plumbing",
            name="descriptions",
            field=models.TextField(blank=True, null=True),
        ),
    ]
