# Generated by Django 3.0.14 on 2022-05-25 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0003_student_scholarship_percentage'),
        ('enrollment_management', '0007_auto_20220113_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='system_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management.student'),
        ),
    ]
