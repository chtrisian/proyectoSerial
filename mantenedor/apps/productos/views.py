from django.shortcuts import render
from .models import Producto

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html', {})

def shop(request):
	productos = Producto.objects.all()
	return render (request, 'producto/tienda.html',{'productos':productos})

