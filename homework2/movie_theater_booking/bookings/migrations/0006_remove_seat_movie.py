# Generated by Django 4.2.11 on 2025-03-05 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_seat_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='movie',
        ),
    ]
