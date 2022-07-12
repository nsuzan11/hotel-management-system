# Generated by Django 4.0.6 on 2022-07-12 13:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=15)),
                ('opening_hour', models.CharField(max_length=15)),
                ('closing_hour', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('footer_text', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Hotel',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_menu', models.CharField(max_length=30)),
                ('bar_menu', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=30, unique=True)),
                ('room_price', models.PositiveIntegerField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('start_day', models.DateField(verbose_name='start date AD')),
                ('end_day', models.DateField(verbose_name='end date AD')),
                ('no_people', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinValueValidator(10)])),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.room')),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bill',
            },
        ),
    ]
