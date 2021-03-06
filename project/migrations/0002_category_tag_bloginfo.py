# Generated by Django 4.0.1 on 2022-03-26 02:51

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Category name')),
                ('describe', models.CharField(max_length=100, null=True, verbose_name='descitbe')),
            ],
            options={
                'verbose_name': 'project category form',
                'verbose_name_plural': 'project category form',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Tag name')),
                ('describe', models.CharField(max_length=100, null=True, verbose_name='describe')),
            ],
            options={
                'verbose_name': 'project tag form',
                'verbose_name_plural': 'project tag form',
            },
        ),
        migrations.CreateModel(
            name='Bloginfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='project title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='project body')),
                ('created_time', models.DateTimeField(verbose_name='created time')),
                ('modified_time', models.DateTimeField(verbose_name='last modified time')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='project excerpt')),
                ('views', models.IntegerField(default=0, verbose_name='views')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.category', verbose_name='category')),
                ('tags', models.ManyToManyField(blank=True, to='project.Tag', verbose_name='project tags')),
            ],
            options={
                'verbose_name': 'project form',
                'verbose_name_plural': 'project form',
                'ordering': ['-created_time'],
            },
        ),
    ]
