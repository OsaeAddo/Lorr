from django.urls import path

from .views import HomeView, ProductView, add_to_cart, remove_from_cart

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product/<pk>/', ProductView.as_view(), name="product"),
    path('add-to-cart/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<pk>', remove_from_cart, name="remove-from-cart")
]