from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Producto
from allauth.account.forms import SignupForm


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = [
            'nombreProducto', 'descripcionProducto', 'categoria',
            'imagenProducto'
        ]


class MyCustomSignupForm(SignupForm):

    first_name = forms.CharField(
        max_length=30,
        label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(
        max_length=30,
        label='Apellido',
        widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user