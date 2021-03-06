# Generated by Django 3.1.2 on 2020-12-15 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='商品数量')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
                'ordering': ['-ctime'],
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(default='', max_length=30, unique=True, verbose_name='订单编号')),
                ('pay_status', models.CharField(default='Paying', max_length=16, verbose_name='订单状态')),
                ('pay_type', models.CharField(choices=[('alipay', '支付宝'), ('wechat', '微信')], default='alipay', max_length=16, verbose_name='支付类型')),
                ('order_message', models.CharField(default='', max_length=200, verbose_name='订单留言')),
                ('order_amount', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('status_time', models.DateTimeField(blank=True, null=True, verbose_name='支付时间或手动取消')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'ordering': ['-ctime'],
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField(default=0, verbose_name='商品数量')),
                ('checked', models.BooleanField(default=False, verbose_name='是否选中')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('goods', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '购物车喵',
                'verbose_name_plural': '购物车喵',
                'ordering': ['-ctime'],
            },
        ),
    ]
