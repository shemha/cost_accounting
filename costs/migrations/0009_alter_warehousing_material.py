# Generated by Django 3.2.7 on 2021-10-06 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0008_warehousing_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousing',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='costs.material'),
        ),
    ]