from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario=models.IntegerField(primary_key=True, verbose_name='Id de usuario')
    emailUsuario=models.CharField(max_length=50, verbose_name='email de usuario')
    nombreUsuario=models.CharField(max_length=50, verbose_name='nombre de usuario')
    passwordUsuario=models.CharField(max_length=50, verbose_name='nombre de usuario')
    
    def __str__(self):
        return self.emailUsuario
    
class Mensaje(models.Model):
    idMensaje=models.IntegerField(primary_key=True, verbose_name='Id de mensaje')
    contMensaje=models.CharField(max_length=1000, verbose_name='contenido del mensaje')
    Usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contMensaje
    
class CategoriaProducto(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='id de categoria')
    nombreCategoria=models.CharField(max_length=50, verbose_name='nombre categoria')
    
    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True, verbose_name='id de Producto')
    nombreProducto=models.CharField(max_length=50, verbose_name='nombre Producto')
    descripcionProducto=models.CharField(max_length=200, verbose_name='descripcion Producto')
    categoria=models.ForeignKey(CategoriaProducto, default=1, on_delete=models.CASCADE)
    imagenProducto=models.ImageField(upload_to='uploads', blank=True, verbose_name='Imagen Producto')
    
    def __str__(self):
        return self.nombreProducto
    

    
    

    
