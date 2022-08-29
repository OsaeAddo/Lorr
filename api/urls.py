from django.urls import path


router = SimpleRouter()
router.register("prodoucts", ProductViewSet, basename="products")



urlpatterns = [
    path('', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
