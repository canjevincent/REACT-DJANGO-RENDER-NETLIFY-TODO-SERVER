# Generated by Django 4.2.6 on 2023-10-24 17:40

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(default=None, max_length=200, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ,.-]*$', 'Only Alpha, numeric, dash, comma, dot and spaces are allowed.')])),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
