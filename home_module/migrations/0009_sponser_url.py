# Generated by Django 4.1.6 on 2023-03-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0008_sponser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponser',
            name='url',
            field=models.URLField(blank=True, max_length=150, null=True, verbose_name='آدرس سایت شرکت ( اختیاری )'),
        ),
    ]
