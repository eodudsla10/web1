from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import shop

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def createshop(request):
    shopcontent = request.POST['shopcontent']
    new_shop = shop(content=shopcontent)
    new_shop.save()
    return HttpResponseRedirect(reverse("contact")) 

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def single_product(request):
    return render(request, 'single-product.html')

def single_product2(request):
    return render(request, 'single-product2.html')

def single_product3(request):
    return render(request, 'single-product3.html')

def single_product4(request):
    return render(request, 'single-product4.html')

