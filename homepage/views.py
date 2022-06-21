from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def home(request):
    
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'homepage/index.html', datos)

def lista_mod(request):
    
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'homepage/lista_mod.html', datos)

def forma_producto(request):
    
    datos = {
        'form': ProductoForm()
    }
    
    if (request.method == 'POST'):
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
        else:
    
            datos['mensaje'] = 'No se guardó producto'
    return render(request, 'homepage/forma_producto.html', datos)

def modificar_producto(request, id):
    producto=Producto.objects.get(idProducto=id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if (request.method == 'POST'):
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Producto se modificó'
        else:
            datos['mensaje'] = 'Producto NO se modificó'

    return render(request, 'homepage/modificar_producto.html', datos)

def eliminar_producto(request, id):
    producto= Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(to='lista_mod')
            

