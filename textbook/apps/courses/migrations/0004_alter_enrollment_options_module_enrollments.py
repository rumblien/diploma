# Generated by Django 4.1.3 on 2023-02-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_enrollment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AddField(
            model_name='module',
            name='enrollments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_enrollments', to='courses.enrollment'),
        ),
    ]
