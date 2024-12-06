# Generated by Django 5.1.1 on 2024-12-06 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Businesses", "0004_alter_business_user_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="business_user",
            name="description",
        ),
        migrations.RemoveField(
            model_name="business_user",
            name="location",
        ),
        migrations.RemoveField(
            model_name="business_user",
            name="rating",
        ),
        migrations.RemoveField(
            model_name="business_user",
            name="type",
        ),
        migrations.CreateModel(
            name="Business",
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
                ("image", models.URLField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                ("whatsapp_link", models.URLField(blank=True, null=True)),
                ("phone", models.CharField(max_length=20)),
                (
                    "type",
                    models.CharField(
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
                ("address", models.CharField(max_length=255)),
                (
                    "rating",
                    models.DecimalField(decimal_places=1, default=0, max_digits=2),
                ),
                ("link", models.TextField(blank=True, max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("descriptions", models.TextField(blank=True, null=True)),
                ("location", models.CharField(max_length=255)),
                ("lat_long", models.CharField(max_length=25)),
                (
                    "business_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="businesses",
                        to="Businesses.business_user",
                    ),
                ),
            ],
        ),
    ]