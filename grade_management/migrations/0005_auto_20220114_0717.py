# Generated by Django 3.0.11 on 2022-01-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_management', '0004_auto_20220114_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='trimester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grades',
            name='year',
            field=models.IntegerField(),
        ),
    ]
