# Generated by Django 4.1.6 on 2023-03-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0003_delete_supportserviceimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='images/favicon', verbose_name='فوآیکن ( Favicon )'),
        ),
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(blank=True, choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزییات محصولات'), ('home_page', 'صفحه اصلی')], max_length=100, null=True, verbose_name='جایگاه نمایشی'),
        ),
    ]
