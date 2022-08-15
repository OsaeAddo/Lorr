from django.urls import path


from .views import ListItemView, DetailItemView



urlpatterns = [
    path('', ListItemView.as_view()),
    path('item/<int:pk>/', DetailItemView.as_view()),
]
