# Generated by Django 2.1.2 on 2018-12-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_detallecompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='precio_compra',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]