# Generated by Django 3.2.7 on 2021-09-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0005_auto_20210924_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='製品名'),
        ),
    ]
