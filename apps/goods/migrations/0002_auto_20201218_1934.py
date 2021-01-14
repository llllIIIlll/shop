# Generated by Django 3.1.2 on 2020-12-18 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['index'], 'verbose_name': '首页轮播', 'verbose_name_plural': '首页轮播'},
        ),
        migrations.RemoveIndex(
            model_name='goods',
            name='shop_price_idx',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='goods_brief',
            new_name='brief_desc',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='goods_desc',
            new_name='detailed_desc',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='shop_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='goods_num',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='ship_free',
        ),
        migrations.AlterField(
            model_name='banner',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品'),
        ),
        migrations.AddIndex(
            model_name='goods',
            index=models.Index(fields=['price'], name='price_idx'),
        ),
    ]
