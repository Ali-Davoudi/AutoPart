# Generated by Django 4.1.2 on 2022-11-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_module', '0002_customercomment_is_active_reasonchoice_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercomment',
            name='rate',
            field=models.PositiveIntegerField(default=2, verbose_name='امتیاز کاربر به ما'),
            preserve_default=False,
        ),
    ]
