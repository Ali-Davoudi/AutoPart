# Generated by Django 4.1.6 on 2023-02-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0004_suportservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='عنوان')),
                ('sub_title', models.CharField(max_length=40, verbose_name='تعریف')),
                ('image', models.ImageField(upload_to='images/support_services', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'سرویس پشتیبانی',
                'verbose_name_plural': 'سرویس های پشتیبانی',
            },
        ),
        migrations.DeleteModel(
            name='SuportService',
        ),
    ]
