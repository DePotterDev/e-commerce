from django.urls import path
from .views import HomeView, ShopView, ItemDetailView, cart, checkout

app_name = 'core'

urlpatterns = [   
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('carrinho/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
