from django.shortcuts import render
from .models import Goods

# Create your views here.
def post_list(request):

    return render(request, 'blog/post_list.html', {})
def shopping_list(request):
    goods = Goods.objects.all()
    return render(request, 'blog/shopping_list.html', {'goods': goods})