from django.shortcuts import render
from .models import Goods
from .models import Purchase
from django.http import HttpResponse
# Create your views here.
def post_list(request):

    return render(request, 'blog/post_list.html', {'total_count':Purchase.total()})
def shopping_list(request):
    goods = Goods.objects.all()
    if request.method == "POST":
        items = Purchase.objects.filter(goods_id=(request.POST['id']))
        if items:
            items[0].count = items[0].count+1
            items[0].save()
        else:
            allid = Goods.objects.filter(id=(request.POST['id']))
            Purchase.objects.create(goods_id=allid[0].id,
                                    type=allid[0].type,
                                    name=allid[0].name,
                                    price=allid[0].price,
                                    unit=allid[0].unit,
                                    count=1)
        return HttpResponse(Purchase.total())
    return render(request, 'blog/shopping_list.html', {'goods': goods,'total_count' : Purchase.total()})
def shop_cart(request):
    purchase = Purchase.objects.all()

    return render(request, 'blog/shop_cart.html', {'total_count' : Purchase.total(),'purchase':purchase})