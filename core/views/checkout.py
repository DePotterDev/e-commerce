from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from core.models import Item, OrderItem, Order, BillingAddress
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
        try:           
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                CPF = form.cleaned_data.get('CPF')
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                state = form.cleaned_data.get('state')
                city = form.cleaned_data.get('city')
                CEP = form.cleaned_data.get('CEP')
                # TODO: add functionality for these fields 
                # same_shipping_address = form.cleaned_data.get('same_shipping_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user = self.request.user, 
                    street_address = street_address, 
                    apartment_address = apartment_address, 
                    state = state, 
                    city = city, 
                    CEP = CEP, 
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                # TODO: add redirect to the selected payment option
                # print(form.cleaned_data)
                # print("The form is valid")
                return redirect('core:checkout')
            messages.warning(self.request, "Checkout Falhado")
            return redirect('core:checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, "Você não tem um pedido ativo." )
            return redirect("core:cart")         
        print(self.request.POST)
        
