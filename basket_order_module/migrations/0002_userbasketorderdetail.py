# Generated by Django 4.1.6 on 2023-02-16 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_alter_productgallery_options_productcomment'),
        ('basket_order_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBasketOrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_count', models.PositiveIntegerField(verbose_name='تعداد محصول')),
                ('final_price', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='قیمت نهایی تکی محصول')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_module.product', verbose_name='محصول')),
                ('user_basket_order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basket_order_module.userbasketorder', verbose_name='سبد خرید کاربر')),
            ],
            options={
                'verbose_name': 'جزییات سبد خرید کاربر',
                'verbose_name_plural': 'جزییات سبدهای خرید کاربران',
            },
        ),
    ]
