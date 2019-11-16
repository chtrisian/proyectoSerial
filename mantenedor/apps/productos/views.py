from django.shortcuts import render, redirect
from .models import Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProductoForm
# Create your views here.
def main_page(request):
    return render(request, 'main_page.html', {})

def shop(request):
	productos = Producto.objects.all()
	return render (request, 'producto/tienda.html',{'productos':productos})

def producto_view(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/producto_list/')
	else:
		form = ProductoForm()
	return render(request, 'producto/producto_add.html', {'form':form})


def producto_list(request):
	productos = Producto.objects.all().order_by('id')
	return render(request, 'producto/producto_list.html', {'productos':productos})



def producto_edit(request, cod):
	productos = Producto.objects.get(id_producto=cod)
	if request.method == 'GET':
		form = ProductoForm(instance=productos)
	else:
		form = ProductoForm(request.POST, instance=productos)
		if form.is_valid():
			form.save()
		return redirect('/producto_list/')
	return render(request, 'producto/producto_editar.html', {'form':form})



def producto_delete(request, cod):
	productos = Producto.objects.get(id_producto=cod)
	if request.method == 'POST':
		productos.delete()
		return redirect('/producto_list/')
	return render(request, 'producto/producto_delete.html', {'productos':productos})

def shop_mas_vendidos(request):
	productos = Producto.objects.all().filter(id_producto= 4)
	return render (request, 'producto/tienda.html',{'productos':productos})	

def shop_oferta_mes(request):
	productos = Producto.objects.all().filter(id_producto= 5)
	return render (request, 'producto/tienda.html',{'productos':productos})	