from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item


class HomeView(ListView):
    model = Item
    template_name = "home.html"

class ShopView(ListView):
    model = Item
    template_name = "shop.html"

# def product(request):
#     context = {'items': Item.objects.all()}
#     return render(request, "product.html", context)

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")
