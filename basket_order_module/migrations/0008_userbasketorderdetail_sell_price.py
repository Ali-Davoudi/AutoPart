# Generated by Django 4.1.6 on 2023-03-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_order_module', '0007_remove_userbasketorderdetail_sell_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbasketorderdetail',
            name='sell_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
