# Generated by Django 2.2.4 on 2019-09-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20190807_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_level',
            field=models.PositiveIntegerField(verbose_name='stock level'),
        ),
    ]
