from django.db import models
from django.utils import timezone


class Goods(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField(default='')
    unit = models.CharField(max_length=200)

class Purchase(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField(default='')
    unit = models.CharField(max_length=200)
    goods_id = models.DecimalField(decimal_places=0,max_digits=100,default=0)
    count = models.DecimalField(decimal_places=0,max_digits=100,default=0)

    def __str__(self):
        return self.type