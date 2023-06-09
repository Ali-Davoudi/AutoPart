# Generated by Django 4.1.2 on 2022-11-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url_title', models.CharField(max_length=250, verbose_name='عنوان در URL')),
            ],
            options={
                'verbose_name': 'دسته بندی مقاله',
                'verbose_name_plural': 'دسته بندی مقالات',
            },
        ),
    ]
