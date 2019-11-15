from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [   
    path('registro', views.Registro.as_view()),
    path('registro_exitoso', views.registro_exitoso),
]
