# Generated by Django 3.0.11 on 2022-01-13 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum_management', '0001_initial'),
        ('enrollment_management', '0003_enrollment_tuition_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='curriculum_name',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='curriculum_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculum_management.curriculum'),
        ),
    ]
