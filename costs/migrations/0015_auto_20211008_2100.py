# Generated by Django 3.2.7 on 2021-10-08 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0014_auto_20211008_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='client',
        ),
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='costs.customer', verbose_name='得意先'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.material', verbose_name='材料名'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.product', verbose_name='製品名'),
        ),
        migrations.AlterField(
            model_name='material',
            name='division',
            field=models.CharField(choices=[('FD', '原材料'), ('PT', '部品'), ('SD', '補助資材'), ('XX', 'その他')], max_length=2, verbose_name='区分'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit',
            field=models.CharField(choices=[('GR', 'グラム'), ('KG', 'キログラム'), ('CM', 'センチメートル'), ('MT', 'メートル'), ('ML', 'ミリリットル'), ('LT', 'リットル'), ('QT', '個数')], max_length=2, verbose_name='単位'),
        ),
        migrations.AlterField(
            model_name='material',
            name='vender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.vender', verbose_name='仕入先'),
        ),
        migrations.AlterField(
            model_name='orderer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.customer', verbose_name='会社名'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.category', verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='product',
            name='division',
            field=models.CharField(choices=[('HD', '手渡し'), ('DV', '配送'), ('CR', '搬入'), ('XX', 'その他')], max_length=2, verbose_name='分類'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('GR', 'グラム'), ('KG', 'キログラム'), ('CM', 'センチメートル'), ('MT', 'メートル'), ('ML', 'ミリリットル'), ('LT', 'リットル'), ('QT', '個数')], max_length=2, verbose_name='単位'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='giving_date',
            field=models.DateTimeField(verbose_name='引き渡し日'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='order_date',
            field=models.DateField(verbose_name='注文日'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.product', verbose_name='製品名'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='settlement',
            field=models.CharField(choices=[('CA', '現金決済'), ('CC', 'クレジットカード決済'), ('RC', '掛取引'), ('AN', 'その他')], max_length=2, verbose_name='決済方法'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='warehousing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.warehousing', verbose_name='材料名'),
        ),
        migrations.AlterField(
            model_name='warehousing',
            name='cost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.cost', verbose_name='原価'),
        ),
    ]
