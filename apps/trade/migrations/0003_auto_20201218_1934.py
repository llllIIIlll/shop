# Generated by Django 3.1.2 on 2020-12-18 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0002_auto_20201218_1934'),
        ('trade', '0002_auto_20201215_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ['-ctime'], 'verbose_name': '购物车', 'verbose_name_plural': '购物车'},
        ),
        migrations.RemoveField(
            model_name='ordergoods',
            name='goods_num',
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='nums',
            field=models.IntegerField(default=1, verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='status_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='支付时间或手动取消的时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='nums',
            field=models.IntegerField(default=1, verbose_name='商品数量'),
        ),
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together={('user', 'goods')},
        ),
    ]
