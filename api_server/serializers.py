from rest_framework import serializers
from .models import Sale, ProductType


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = ('product_name', 'product_title', 'product_price', 'units', 'pay_received', 'cost', 'date')


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ('name', 'title', 'image', 'price')
