# Generated by Django 3.2.7 on 2021-10-13 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0020_auto_20211013_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='defective',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='仕損じ量'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='work_in_process',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='仕掛量'),
        ),
    ]