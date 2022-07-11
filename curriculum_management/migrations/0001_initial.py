# Generated by Django 3.0.11 on 2021-09-10 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=150)),
                ('remarks', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='curriculum_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=150)),
                ('subject_name', models.CharField(max_length=150)),
                ('unit', models.IntegerField()),
                ('year', models.CharField(max_length=150)),
                ('trimester', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('curriculum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum_management.curriculum')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
