# Generated by Django 3.0.11 on 2021-10-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='miscellaneous',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='nstp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
