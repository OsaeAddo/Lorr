from django.urls import path


from .views import ItemApiView



urlpatterns = [
    path('', ItemApiView.as_view()),
]
