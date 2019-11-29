import json
from django.shortcuts import render, redirect
from .models import Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProductoForm
from .serializers import ProductSerializer 
from rest_framework import generics
# Create your views here.
class ProductViewSet(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset= Producto.objects.all()
        serializer_class= ProductSerializer


def main_page(request):
    return render(request, 'main_page.html', {})

def shop(request):
	productos = Producto.objects.all()
	return render (request, 'producto/tienda.html',{'productos':productos})

def producto_view(request):
	user = request.user
	if user.has_perm('productos.Staff'):
		if request.method == 'POST':
			form = ProductoForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
			return redirect('/producto_list/')
		else:
			form = ProductoForm()
		return render(request, 'producto/producto_add.html', {'form':form})
	else:
		return redirect('/')

def producto_list(request):
	user = request.user
	if user.has_perm('productos.Staff'):
		productos = Producto.objects.all().order_by('id')
		return render(request, 'producto/producto_list.html', {'productos':productos})
	else:
		return redirect('/')

def producto_edit(request, cod):
	user = request.user
	if user.has_perm('productos.Staff'):
		productos = Producto.objects.get(id_producto=cod)
		if request.method == 'GET':
			form = ProductoForm(instance=productos)
		else:
			form = ProductoForm(request.POST, request.FILES,instance=productos)
			if form.is_valid():
				form.save()
			return redirect('/producto_list/')
		return render(request, 'producto/producto_editar.html', {'form':form})
	else:
		return redirect('/')

def producto_delete(request, cod):
	user = request.user
	if user.has_perm('productos.Staff'):
		productos = Producto.objects.get(id_producto=cod)
		if request.method == 'POST':
			productos.delete()
			return redirect('/producto_list/')
		return render(request, 'producto/producto_delete.html', {'productos':productos})
	else:
		return redirect('/')


def shop_mas_vendidos(request):
	productos = Producto.objects.all().filter(id_producto= 4)
	return render (request, 'producto/tienda.html',{'productos':productos})	

def shop_oferta_mes(request):
	productos = Producto.objects.all().filter(id_producto= 5)
	return render (request, 'producto/tienda.html',{'productos':productos})	