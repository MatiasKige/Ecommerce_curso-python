# Generated by Django 4.2.2 on 2023-08-02 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
