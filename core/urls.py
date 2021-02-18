from django.urls import path
from .views import cart, checkout, home, product, shop


# (
#     HomeView, 
#     ShopView,
#     ItemDetailView,
#     add_to_cart,
#     remove_from_cart,
#     remove_single_item_from_cart,
#     OrderSummaryView,
#     checkout
# )

app_name = 'core'

urlpatterns = [   
    path('', home.HomeView.as_view(), name='home'),
    path('shop/', shop.ShopView.as_view(), name='shop'),
    path('product/<slug>/', product.ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', cart.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', cart.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', cart.remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('carrinho/', cart.OrderSummaryView.as_view(), name='cart'),
    path('checkout/', checkout.CheckoutView.as_view(), name='checkout'),
]
