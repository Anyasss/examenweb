# Generated by Django 2.1.2 on 2018-12-06 20:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_producto_lista'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Producto'),
        ),
        migrations.AlterField(
            model_name='lista',
            name='costoPresupuestado',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='lista',
            name='costoReal',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='lista',
            name='nombre',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='lista',
            name='totalAgregados',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='lista',
            name='totalComprados',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='costoPresupuestado',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='costoReal',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]