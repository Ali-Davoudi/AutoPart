# Generated by Django 4.1.6 on 2023-02-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(blank=True, null=True, verbose_name='فعال / غیرفعال'),
        ),
    ]
