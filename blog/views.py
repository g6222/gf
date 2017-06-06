from django.shortcuts import render
from .models import Goods
from .models import Purchase
from django.http import HttpResponse
from django.http import JsonResponse
import time
# Create your views here.
def post_list(request):

    return render(request, 'blog/post_list.html', {'total_count': Purchase.total()})
def shopping_list(request) :
    goods = Goods.objects.all()
    if request.method == "POST":
        items = Purchase.objects.filter(goods_id=(request.POST['id']))
        if items:
            items[0].count = items[0].count+1
            items[0].subtotal = items[0].price*items[0].count
            items[0].totals = items[0].subtotal
            items[0].save()
        else:
            allid = Goods.objects.filter(id=(request.POST['id']))
            Purchase.objects.create(goods_id=allid[0].id,
                                    type=allid[0].type,
                                    name=allid[0].name,
                                    price=allid[0].price,
                                    unit=allid[0].unit,
                                    free=allid[0].free,
                                    count=1)
        return HttpResponse(Purchase.total())
    return render(request, 'blog/shopping_list.html', {'goods': goods,'total_count': Purchase.total()})
def shop_cart(request):
    purchase = Purchase.objects.all()
    totals = Purchase.shop_total()
    if request.method == "POST":
        items = request.POST['quantity']
        sub_total= Purchase.objects.filter(goods_id=(request.POST['id']))
        if sub_total:
            sub_total[0].count = sub_total[0].count+int(items)
            sub_total[0].subtotal = sub_total[0].price * sub_total[0].count
            if sub_total[0].free == 1:
                sub_total[0].free_count = int(sub_total[0].count / 3)
                sub_total[0].free_counts = sub_total[0].subtotal - (sub_total[0].free_count * sub_total[0].price)
                sub_total[0].free_moeny = sub_total[0].free_count * sub_total[0].price
            sub_total[0].save()
            if sub_total[0].count == 0:
                sub_total[0].delete()
        return JsonResponse({'total_count': Purchase.total(), 'total': sub_total[0].subtotal,'number': sub_total[0].count,'totals': totals,
                             'free': sub_total[0].free_counts,'free_count':sub_total[0].free_count,'moeny':sub_total[0].free_moeny})
    return render(request, 'blog/shop_cart.html', {'total_count': Purchase.total(), 'purchase': purchase,'totals':Purchase.shop_total()})
def payment(request):
    purchase = Purchase.objects.all()
    moeny = Purchase.shop_moeny()
    if request.method == 'POST':
        Purchase.objects.all().delete()

    local = time.strftime("%Y年%m月%d号 %X ", time.localtime())
    return render(request, 'blog/payment.html', {'total_count':Purchase.total(),'purchase': purchase,'totals':Purchase.shop_total(),'local':local,'moeny':Purchase.shop_moeny()})