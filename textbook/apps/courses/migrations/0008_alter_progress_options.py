# Generated by Django 4.1.3 on 2023-02-24 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_progress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name': 'Пргоресс', 'verbose_name_plural': 'Прогрессы'},
        ),
    ]
