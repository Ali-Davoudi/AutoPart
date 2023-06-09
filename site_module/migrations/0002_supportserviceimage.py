# Generated by Django 4.1.6 on 2023-02-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='عنوان آیکن')),
                ('image', models.ImageField(upload_to='images/support_services', verbose_name='تضویر')),
            ],
            options={
                'verbose_name': 'تصویر پشتیبانی سرویس',
                'verbose_name_plural': 'تصویرهای پشتیبانی سسرویس ها',
            },
        ),
    ]
