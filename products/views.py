from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import products
from .serializers import ProductsSerializer
from .models import Products



@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer._data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def products_detail(request, pk):
    try:
        car = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(products);
        return Response(serializer._data)
        
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);
