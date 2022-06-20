from dataclasses import fields
from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','title','description','inventory_quantity','price']