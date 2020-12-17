from django.urls import path
from .views import home, shop, product, cart, checkout

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('product/', product, name='product'),
    path('carrinho/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
