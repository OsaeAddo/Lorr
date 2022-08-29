from django.urls import path


router = SimpleRouter()
router.register("products", ProductViewSet, basename="products")
router.register("orders", OrderViewSet, basename="orders")



urlpatterns = [
    path('', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
