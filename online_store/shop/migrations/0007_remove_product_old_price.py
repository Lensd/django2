# Generated by Django 4.0 on 2022-03-23 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_old_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='old_price',
        ),
    ]
