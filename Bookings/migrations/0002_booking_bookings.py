# Generated by Django 5.1.1 on 2024-11-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Bookings", "0001_initial"),
        ("User", "0002_remove_commonuser_bookings"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="bookings",
            field=models.ManyToManyField(
                related_name="booked_user", to="User.commonuser"
            ),
        ),
    ]
