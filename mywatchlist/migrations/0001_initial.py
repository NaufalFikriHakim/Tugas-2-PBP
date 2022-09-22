# Generated by Django 4.1 on 2022-09-22 02:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField(default=False)),
                ('title', models.TextField()),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('release_date', models.DateField()),
                ('review', models.TextField()),
            ],
        ),
    ]