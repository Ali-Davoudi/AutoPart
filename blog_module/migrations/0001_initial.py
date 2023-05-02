# Generated by Django 4.1.2 on 2022-11-23 12:09

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='عنوان')),
                ('short_description', ckeditor.fields.RichTextField(verbose_name='توضیحات کوتاه')),
                ('description', ckeditor.fields.RichTextField(verbose_name='متن اصلی مقاله')),
                ('image', models.ImageField(upload_to='images/articles', verbose_name='تصویر')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / حذف نشده')),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]