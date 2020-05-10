from django.shortcuts import render
from .models import Product
# Create your views here.



def product_list(request):
    all_products = Product.objects.all()
    return render(request,'products/all_products.html',{'products' :all_products })


def product_detail(request , id):
    product_detail = Product.objects.get(id=id)
    return render(request,'products/product_detail.html',{'product' : product_detail})