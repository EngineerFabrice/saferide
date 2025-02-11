# Generated by Django 5.1.3 on 2024-11-23 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('license_number', models.CharField(max_length=50)),
                ('car_owner_name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('role', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('can_register', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.driver')),
                ('drop_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drop_location', to='myApp.location')),
                ('pickup_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pickup_location', to='myApp.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('rating', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.booking')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
        ),
    ]
