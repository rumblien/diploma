# Generated by Django 4.1.3 on 2023-02-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_progress_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='file',
            field=models.FileField(null=True, upload_to='', verbose_name='Файл'),
        ),
    ]
