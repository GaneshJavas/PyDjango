# Generated by Django 4.2.16 on 2024-11-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EMS_User',
            new_name='Attendees',
        ),
        migrations.AlterField(
            model_name='venue',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Website'),
        ),
    ]
