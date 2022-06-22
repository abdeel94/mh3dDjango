from rest_framework import serializers
from homepage.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','descripcionProducto','categoria','imagenProducto',]
