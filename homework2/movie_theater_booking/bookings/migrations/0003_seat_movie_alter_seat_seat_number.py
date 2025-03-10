# Generated by Django 4.2.11 on 2025-03-05 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_remove_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='bookings.movie'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(max_length=5),
        ),
    ]
