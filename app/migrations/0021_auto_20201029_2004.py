# Generated by Django 3.1.1 on 2020-10-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20201029_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='likes',
            new_name='liked',
        ),
    ]
