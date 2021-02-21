from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from core.models import Item, OrderItem, Order
from django.shortcuts import redirect
from django.utils import timezone
from ..forms import CheckoutForm

class CheckoutView(View):
    def get(self, *args, **kwargs):
        # form
        form = CheckoutForm()
        context = {
            'form':form
        }
        return render(self.request, "checkout.html", context)
    def post(self,*args,**kwargs):
        form = CheckoutForm(self.request.POST or None)
        print(self.request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("O formulário é válido.")
            return redirect('core:checkout')
        messages.warning(self.request, "Checkout Falhado")
        return redirect('core:checkout')
