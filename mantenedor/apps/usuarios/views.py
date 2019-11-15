from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegistroForm
# Create your views here.
class Registro(CreateView):
	model = User
	template_name = "usuario/registro.html"
	form_class = RegistroForm
	success_url = "/accounts/registro_exitoso"

def registro_exitoso(request):
    return render(request, 'usuario/registro_exitoso.html', {})