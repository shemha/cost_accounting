# Generated by Django 3.2.7 on 2021-09-22 11:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, verbose_name='会社名')),
                ('name', models.CharField(max_length=50, verbose_name='担当者名')),
                ('post', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=100, verbose_name='住所')),
                ('tel', models.CharField(max_length=11, verbose_name='電話番号')),
                ('fax', models.CharField(blank=True, max_length=10, verbose_name='FAX番号')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('entry', models.DateTimeField(auto_now=True, verbose_name='登録日')),
                ('note', models.TextField(blank=True, verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='使用量')),
                ('work_in_process', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='仕掛量')),
                ('defective', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='仕損じ量')),
                ('term_begin', models.DateTimeField(auto_now=True, verbose_name='開始日')),
                ('term_end', models.DateTimeField(auto_now=True, verbose_name='締め日')),
                ('cost_note', models.TextField(blank=True, verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='製品名')),
                ('unit', models.PositiveIntegerField(verbose_name='製品単位')),
                ('amount', models.PositiveIntegerField(verbose_name='セット数')),
                ('note', models.TextField(blank=True, verbose_name='備考')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.category')),
            ],
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, verbose_name='会社名')),
                ('name', models.CharField(max_length=50, verbose_name='担当者名')),
                ('post', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=100, verbose_name='住所')),
                ('tel', models.CharField(max_length=11, verbose_name='電話番号')),
                ('fax', models.CharField(blank=True, max_length=10, verbose_name='FAX番号')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('entry', models.DateTimeField(auto_now=True, verbose_name='登録日')),
                ('note', models.TextField(blank=True, verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='Warehousing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='入庫日')),
                ('quantity', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='入庫量')),
                ('unit', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.cost')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='仕入数量')),
                ('note', models.TextField(blank=True, verbose_name='備考')),
                ('warehousing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.warehousing')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('order_amount', models.PositiveIntegerField(default=0, verbose_name='注文数')),
                ('settlement', models.PositiveIntegerField(verbose_name='決済区分')),
                ('total_price', models.PositiveIntegerField(verbose_name='販売価額')),
                ('sales_tax', models.PositiveIntegerField(verbose_name='消費税額')),
                ('commission', models.PositiveIntegerField(verbose_name='その他手数料')),
                ('how_to_give', models.PositiveIntegerField(verbose_name='引き渡し方法')),
                ('giving_date', models.DateTimeField(auto_now=True, verbose_name='引き渡し日')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.product')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='材料名')),
                ('note', models.TextField(blank=True, verbose_name='備考')),
                ('vender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.vender')),
            ],
        ),
        migrations.AddField(
            model_name='cost',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.material'),
        ),
        migrations.AddField(
            model_name='cost',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.product'),
        ),
    ]