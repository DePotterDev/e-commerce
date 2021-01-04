from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
from django.shortcuts import redirect
from django.utils import timezone

class HomeView(ListView):
    model = Item
    template_name = "home.html"

class ShopView(ListView):
    model = Item
    template_name = "shop.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Este item foi atualizado no seu carrinho.")
            return redirect("core:product", slug=slug)
        else:
            messages.info(request, "Este item foi adicionado ao seu carrinho.")
            order.items.add(order_item)
            return redirect("core:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Este item foi adicionado ao seu carrinho.")
        return redirect("core:product", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "Este item foi removido do seu carrinho.")
            return redirect("core:product", slug=slug)
        else:
            return redirect("core:product", slug=slug)
            messages.info(request, "Este item não estava no seu carrinho.")
    else:
        messages.info(request, "Não há ordem.")
        return redirect("core:product", slug=slug)


def checkout(request):
    return render(request, "checkout.html")

