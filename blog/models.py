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
    goods_id = models.IntegerField(default=0,null=False)
    count = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return self.type

    def total():
        total_count = 0
        self = Purchase.objects.all()
        for items in self:
            total_count += items.count
        return total_count
    def s():
        sub_total = Purchase.price
