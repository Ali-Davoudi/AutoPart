# Generated by Django 4.1.2 on 2023-02-03 16:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('telephone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[utils.validators.validate_email], verbose_name='ایمیل')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'اطلاع تماس',
                'verbose_name_plural': 'اطلاعات تماس برای درج در سایت',
            },
        ),
        migrations.CreateModel(
            name='FooterCategoryTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_category_title', models.CharField(max_length=80, verbose_name='عنوان دسته بندی')),
            ],
            options={
                'verbose_name': 'عنوان دسته بندی لینک Footer سایت',
                'verbose_name_plural': 'عنوان دسته بندی های لینک های Footer سایت',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('header', ckeditor.fields.RichTextField(verbose_name='عنوان سیاست حریم خصوصی')),
                ('description', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'سیاست حریم خصوصی',
                'verbose_name_plural': 'سیاست های حریم خصوصی',
            },
        ),
        migrations.CreateModel(
            name='ServiceIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200, verbose_name='کلاس آیکن')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان آیکن')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'مدیریت آیکن بخش سرویس',
                'verbose_name_plural': 'مدیریت آیکن های بخش سرویس',
            },
        ),
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url', models.URLField(verbose_name='آدرس URL')),
                ('image', models.ImageField(upload_to='images/site_banners', verbose_name='تصویر')),
                ('position', models.CharField(blank=True, choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزییات محصولات'), ('about_us', 'صفحه درباره ما')], max_length=100, null=True, verbose_name='جایگاه نمایشی')),
                ('top_position', models.CharField(blank=True, choices=[('product_list', 'بالای صفحه لیست محصولات')], max_length=100, null=True, verbose_name='جایگاه نمایشی در بالای صفحه')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'بنر تبلیغاتی',
                'verbose_name_plural': 'بنرهای تبلیغاتی',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('logo', models.ImageField(upload_to='images/site_logo', verbose_name='لوگوی شرکت')),
                ('instagram', models.CharField(blank=True, max_length=150, null=True, verbose_name='آی دی اینستاگرام')),
                ('twitter', models.CharField(blank=True, max_length=150, null=True, verbose_name='آی دی توییتر')),
                ('about_company', ckeditor.fields.RichTextField(verbose_name='درباره شرکت')),
                ('copyright', ckeditor.fields.RichTextField(verbose_name='متن کپی رایت')),
            ],
            options={
                'verbose_name': 'مشخصه کلی سایت',
                'verbose_name_plural': 'مشخصات کلی سایت',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='عنوان')),
                ('url', models.URLField(verbose_name='نشانی وب')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('footer_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_module.footercategorytitle', verbose_name='عنوان دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک Footer سایت',
                'verbose_name_plural': 'لینک های Footer سایت',
            },
        ),
    ]