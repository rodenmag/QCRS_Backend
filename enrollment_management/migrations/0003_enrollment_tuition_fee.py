# Generated by Django 3.0.11 on 2021-11-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment_management', '0002_auto_20211001_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='tuition_fee',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
