# Generated by Django 3.1.1 on 2020-12-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20201202_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='fire.png', upload_to='images'),
        ),
    ]