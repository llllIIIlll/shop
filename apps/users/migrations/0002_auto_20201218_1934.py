# Generated by Django 3.1.2 on 2020-12-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]