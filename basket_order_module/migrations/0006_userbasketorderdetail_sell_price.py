# Generated by Django 4.1.6 on 2023-03-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_order_module', '0005_alter_userbasketorder_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbasketorderdetail',
            name='sell_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
