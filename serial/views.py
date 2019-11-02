from django.shortcuts import render
from .models import Usuario, Producto

# Create your views here.
def main_page(request):
    return render(request, 'serial/main_page.html', {})


def register(request):
    return render(request, 'serial/register.html', {})

def shop(request):
	productos = Producto.objects.all()
	return render (request, 'serial/tienda.html',{'productos':productos})

