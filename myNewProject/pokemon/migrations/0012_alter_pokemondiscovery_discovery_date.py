# Generated by Django 4.2.16 on 2024-11-09 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0011_alter_pokemondiscovery_discovery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemondiscovery',
            name='discovery_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 9, 13, 39, 10, 270194, tzinfo=datetime.timezone.utc)),
        ),
    ]
