from django.urls import path
from .views import home, forma_producto, modificar_producto, eliminar_producto, lista_mod
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home ,name="home"),
    path('forma_producto', forma_producto, name="forma_producto"),
    path('modificar_producto/<id>', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>', eliminar_producto, name="eliminar_producto"),
    path('lista_mod', lista_mod ,name="lista_mod"),
    path('logout', LogoutView.as_view()),
    
    
]
