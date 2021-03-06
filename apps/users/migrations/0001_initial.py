# Generated by Django 3.1.2 on 2020-12-15 13:29

import apps.users.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('avatar', models.ImageField(default='users/1.jpeg', upload_to='users/', verbose_name='头像')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活状态')),
                ('is_staff', models.BooleanField(default=False, verbose_name='是否能进入admin界面')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'ordering': ['-ctime'],
            },
            managers=[
                ('objects', apps.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=256, verbose_name='详细地址')),
                ('signer', models.CharField(default='', max_length=100, verbose_name='签收人')),
                ('phone', models.CharField(default='', max_length=11, verbose_name='电话')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认地址')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
                'ordering': ['-ctime'],
            },
        ),
        migrations.AddIndex(
            model_name='useraddress',
            index=models.Index(fields=['phone'], name='phone_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['username'], name='name_idx'),
        ),
    ]
