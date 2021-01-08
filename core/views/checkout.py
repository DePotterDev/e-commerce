from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from core.models import Item, OrderItem, Order
from django.shortcuts import redirect
from django.utils import timezone

def check_out(request):
    return render(request, "checkout.html")