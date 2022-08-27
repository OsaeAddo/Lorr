from django.urls import path

from .views import (
    HomeView, ProductView, OrderSummaryView, 
    add_to_cart, remove_from_cart, reduce_item_quantity
)


app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product/<pk>/', ProductView.as_view(), name="product"),
    path('add-to-cart/<pk>', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<pk>', remove_from_cart, name="remove-from-cart"),
    path('order-summary/', OrderSummaryView.as_view(), name="order-summary"),
    path('reduce-item-quantity/<pk>/', reduce_item_quantity, name="reduce-item-quantity")
    
]