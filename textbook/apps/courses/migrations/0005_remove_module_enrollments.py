# Generated by Django 4.1.3 on 2023-02-19 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_enrollment_options_module_enrollments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='enrollments',
        ),
    ]