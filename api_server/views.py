from rest_framework import viewsets

from .serializers import SaleSerializer, ProductTypeSerializer
from .models import Sale, ProductType


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('product_name')
    serializer_class = SaleSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all().order_by('name')
    serializer_class = ProductTypeSerializer
