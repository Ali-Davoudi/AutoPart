# Generated by Django 4.1.2 on 2022-12-13 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0009_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='verify',
            new_name='is_verify',
        ),
    ]
