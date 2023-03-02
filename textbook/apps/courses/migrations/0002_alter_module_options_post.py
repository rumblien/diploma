# Generated by Django 4.1.3 on 2023-02-16 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order_id'], 'verbose_name': 'Модуль', 'verbose_name_plural': 'Модули'},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_draft', models.BooleanField(default=True, verbose_name='Черновик')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='posts_tag', to='courses.tag')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]