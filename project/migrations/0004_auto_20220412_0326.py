# Generated by Django 3.2.6 on 2022-04-12 03:26

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_category_describe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloginfo',
            options={'ordering': ['-created_time'], 'verbose_name': 'project form', 'verbose_name_plural': 'project form'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'project category form', 'verbose_name_plural': 'project category form'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'project tag form', 'verbose_name_plural': 'project tag form'},
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='project body'),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200, verbose_name='project excerpt'),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='tags',
            field=models.ManyToManyField(blank=True, to='project.Tag', verbose_name='project tags'),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='title',
            field=models.CharField(max_length=50, verbose_name='project title'),
        ),
    ]
