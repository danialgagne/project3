# Generated by Django 2.2.10 on 2020-03-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='small_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
