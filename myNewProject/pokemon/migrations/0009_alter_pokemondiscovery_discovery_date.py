# Generated by Django 4.2.16 on 2024-11-03 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0008_alter_pokemondiscovery_discovery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemondiscovery',
            name='discovery_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 3, 9, 52, 36, 107569, tzinfo=datetime.timezone.utc)),
        ),
    ]
