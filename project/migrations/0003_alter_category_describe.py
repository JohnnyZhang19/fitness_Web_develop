# Generated by Django 4.0.1 on 2022-04-11 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_category_tag_bloginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='describe',
            field=models.CharField(max_length=100, null=True, verbose_name='describe'),
        ),
    ]