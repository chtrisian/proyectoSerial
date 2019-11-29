from .models import Producto
from rest_framework import serializers

# un serializers sirve para transformar el objeto
# a json y viceversa, esto para la comunicacion de datos

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

