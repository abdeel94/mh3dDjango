# Generated by Django 4.0.4 on 2022-05-23 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_producto_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriaproducto',
            old_name='nombreProducto',
            new_name='nombreCategoria',
        ),
    ]
