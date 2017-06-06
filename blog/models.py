from django.db import models
from django.utils import timezone

class Goods(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField(default='')
    unit = models.CharField(max_length=200)
    free = models.IntegerField(default=0)

    def __str__(self):
        return self.type

class Purchase(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField(default='')
    unit = models.CharField(max_length=200)
    goods_id = models.IntegerField(default=0,null=False)
    count = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0)
    free_counts = models.FloatField(default=0)
    free = models.IntegerField(default=0)
    free_count = models.IntegerField(default=0)
    free_moeny = models.FloatField(default=0)

    def total():
        total_count = 0
        self = Purchase.objects.all()
        for items in self:
            total_count += items.count
        return total_count

    def shop_total():
        totals = 0
        self = Purchase.objects.all()
        for items in self:
            totals += items.subtotal
        return totals

    def shop_moeny():
        moeny = 0
        self = Purchase.objects.all()
        for items in self:
            moeny += items.free_moeny
        return moeny

class Free(models.Model):
    goods_id = models.IntegerField(default=0, null=False)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    count = models.IntegerField(default=0)