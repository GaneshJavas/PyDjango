# Generated by Django 4.2.16 on 2024-11-04 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0009_alter_pokemondiscovery_discovery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemondiscovery',
            name='discovery_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 15, 30, 15, 584755, tzinfo=datetime.timezone.utc)),
        ),
    ]
