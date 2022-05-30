from django.contrib import admin

from .models import Mensaje, Usuario, Producto, CategoriaProducto

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)