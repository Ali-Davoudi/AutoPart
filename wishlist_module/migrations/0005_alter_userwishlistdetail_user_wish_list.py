# Generated by Django 4.1.6 on 2023-02-21 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist_module', '0004_userwishlistdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwishlistdetail',
            name='user_wish_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wishlist_module.userwishlist', verbose_name='کاربر'),
        ),
    ]