# Generated by Django 3.2.7 on 2021-10-13 05:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0018_auto_20211012_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='amount',
        ),
        migrations.AddField(
            model_name='cost',
            name='material_amount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='消費量'),
        ),
        migrations.AddField(
            model_name='cost',
            name='product_amount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='生産量'),
        ),
    ]