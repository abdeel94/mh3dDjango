# Generated by Django 4.0.4 on 2022-05-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de categoria')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='nombre producto')),
                ('descripcionProducto', models.CharField(max_length=200, verbose_name='descripcion producto')),
                ('imagenProducto', models.ImageField(upload_to='')),
            ],
        ),
    ]
