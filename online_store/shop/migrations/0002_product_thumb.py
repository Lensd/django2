# Generated by Django 3.1.1 on 2022-02-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(default='default_product.png', null=True, upload_to=''),
        ),
    ]