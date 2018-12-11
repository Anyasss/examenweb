# Generated by Django 2.1.2 on 2018-12-07 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20181206_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city', to='blog.Ciudad'),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='regi', to='blog.Region'),
        ),
    ]