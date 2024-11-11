# Generated by Django 5.1.1 on 2024-11-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Businesses", "0002_alter_business_user_user_business"),
    ]

    operations = [
        migrations.AddField(
            model_name="business_user",
            name="type",
            field=models.CharField(
                choices=[
                    ("Carpentry", "Carpentry"),
                    ("Plumbing", "Plumbing"),
                    ("Electrician", "Electrician"),
                    ("Masonry", "Masonry"),
                    ("Salon", "Salon"),
                    ("Medical", "Medical"),
                    ("Other", "Other"),
                ],
                default="Other",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="business_user",
            name="slug",
            field=models.SlugField(default="", null=True),
        ),
    ]
