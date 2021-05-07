from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Offer,Cart

def index(request):
    products=Product.objects.all
    return render(request,"index.html",{"products":products})

def index1(request):
    offers=Offer.objects.all
    products=Product.objects.all
    return render(request,"index1.html",{"offers":offers})

def cart(request):
    cart_item=Cart.Objects.all
    return render(request,"cart.html",{"cart_items":cart_item})

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"registration.html")    