from datetime import datetime

from django.db import models


class Sale(models.Model):
    product_name = models.CharField(max_length=50)
    product_title = models.CharField(max_length=50)
    product_price = models.FloatField()
    units = models.IntegerField()
    pay_received = models.FloatField()
    cost = models.FloatField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product_title


class ProductType(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
