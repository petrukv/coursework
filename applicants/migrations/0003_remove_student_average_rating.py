# Generated by Django 4.2.5 on 2023-11-23 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0002_student_average_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='average_rating',
        ),
    ]