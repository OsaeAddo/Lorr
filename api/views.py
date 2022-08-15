from django.shortcuts import render

from rest_framework import generics

from main.models import Item, Order, OrderItem

from .serializers import ItemSerializer


class ListItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    
class DetailItemView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer