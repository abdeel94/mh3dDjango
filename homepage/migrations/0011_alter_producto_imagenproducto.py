# Generated by Django 4.0.4 on 2022-05-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_alter_producto_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
