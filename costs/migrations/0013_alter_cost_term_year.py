# Generated by Django 3.2.7 on 2021-11-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0012_alter_cost_term_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='term_year',
            field=models.CharField(default=1, max_length=4, verbose_name='開始年度'),
            preserve_default=False,
        ),
    ]
