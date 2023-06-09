# Generated by Django 4.1.2 on 2022-11-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='نام کاربر')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل کاربر')),
                ('subject', models.CharField(blank=True, max_length=350, null=True, verbose_name='موضوع پیام')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('response', models.TextField(blank=True, null=True, verbose_name='متن پاسخ پیام توسط ادمین')),
                ('is_read_by_admin', models.BooleanField(verbose_name='خوانده شده / نشده')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس های کاربران',
            },
        ),
    ]
