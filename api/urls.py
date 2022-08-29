from django.urls import path

from rest_framework.routers import SimpleRouter

# from .views import ProductListView, ProductDetailView
from .viewset import OrderViewSet, OrderItemViewSet, ProductViewSet


router = SimpleRouter()
router.register("products", ProductViewSet, basename="products")
router.register("orders", OrderViewSet, basename="orders")
router.register("cart", OrderItemViewSet, basename="cart")

urlpatterns = router.urls


urlpatterns = [
    path('', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
