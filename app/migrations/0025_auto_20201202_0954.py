# Generated by Django 3.1.1 on 2020-12-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_userprofile_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='author',
            field=models.BooleanField(default=False),
        ),
    ]
