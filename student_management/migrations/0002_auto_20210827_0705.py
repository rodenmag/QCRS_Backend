# Generated by Django 3.0.11 on 2021-08-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='brgy',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='city_province',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_contact_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
