from django import forms

from apps.productos.models import Producto
from django.forms import ModelForm

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto

		fields = [
			'id_producto',
			'nombre',
			'precio',
			'stock',
			'equipo'
		]
		labels = {
			'id_producto': 'Id Producto',
			'nombre': 'Nombre',
			'precio': 'Precio',
			'stock': 'Stock',
			'equipo': 'Equipo',
		}
		widgets = {
			'id_producto': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
			'stock': forms.TextInput(attrs={'class':'form-control'}),
			'equipo': forms.TextInput(attrs={'class':'form-control'}),
		}