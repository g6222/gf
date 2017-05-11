from django.shortcuts import render
from .models import Goods
from .models import Purchase

# Create your views here.
def post_list(request):

    return render(request, 'blog/post_list.html', {})
def shopping_list(request):
    goods = Goods.objects.all()
    if request.method == "POST":
        s=Purchase.objects.filter(goods_id=(request.POST('id')))
        if s:
            s[0].count = 1
        else:
            Purchase.objects.create(id="goods.id",type="goods.type",name="goods.name",price="goods.price",unit="goods.unit",count="1")

    return render(request, 'blog/shopping_list.html', {'goods': goods})