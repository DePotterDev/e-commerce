from django.shortcuts import render
from .models import Item

def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)

def shop(request):
    return render(request, "shop.html")

def product(request):
    return render(request, "product.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")
