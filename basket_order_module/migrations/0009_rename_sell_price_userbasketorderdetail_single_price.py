# Generated by Django 4.1.6 on 2023-03-28 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket_order_module', '0008_userbasketorderdetail_sell_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbasketorderdetail',
            old_name='sell_price',
            new_name='single_price',
        ),
    ]
