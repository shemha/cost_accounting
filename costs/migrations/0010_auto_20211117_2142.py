# Generated by Django 3.2.7 on 2021-11-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0009_auto_20211110_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='term_begin',
        ),
        migrations.RemoveField(
            model_name='cost',
            name='term_end',
        ),
        migrations.AddField(
            model_name='cost',
            name='term_month',
            field=models.IntegerField(choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mat'), (4, 'Apl'), (5, 'May'), (6, 'Jon'), (7, 'Jra'), (8, 'Aug'), (9, 'Sep'), (10, 'Oct'), (11, 'Nob'), (12, 'Dec')], default=1, verbose_name='開始月'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cost',
            name='term_year',
            field=models.IntegerField(blank=True, max_length=4, null=True, verbose_name='開始年度'),
        ),
    ]
