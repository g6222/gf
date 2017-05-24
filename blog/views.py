from django.shortcuts import render
from .models import Goods
from .models import Purchase
from .models import Free
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def post_list(request):

    return render(request, 'blog/post_list.html', {'total_count':Purchase.total()})
def shopping_list(request) :
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
            items = Purchase.objects.filter(goods_id=(request.POST['id']))
            if items:
                items[0].subtotal = items[0].price*items[0].count
                items[0].totals = items[0].subtotal
                items[0].save()
        return HttpResponse(Purchase.total())
    return render(request, 'blog/shopping_list.html', {'goods': goods,'total_count': Purchase.total()})
def shop_cart(request):
    purchase = Purchase.objects.all()
    if request.method == "POST":
        items = request.POST['quantity']
        sub_total= Purchase.objects.filter(goods_id=(request.POST['id']))
        if sub_total:
            sub_total[0].count = sub_total[0].count+int(items)
            if sub_total[0].count == 0:
                sub_total[0].delete()
            else:
                sub_total[0].subtotal = sub_total[0].price * sub_total[0].count
                sub_total[0].free_count = int(sub_total[0].count / 3)
                sub_total[0].free_counts = sub_total[0].subtotal - (int(sub_total[0].count / 3) * sub_total[0].price)
                sub_total[0].save()
        totals=Purchase.shop_total()
        return JsonResponse({'total_count': Purchase.total(), 'total': sub_total[0].subtotal, 'number': sub_total[0].count,'totals': totals ,'free':sub_total[0].free_counts})
    return render(request, 'blog/shop_cart.html', {'total_count': Purchase.total(), 'purchase': purchase,'totals':Purchase.shop_total()})