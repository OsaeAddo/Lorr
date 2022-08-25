from django.shortcuts import render

from rest_framework import generics

from main.models import Item, Order, OrderItem

from .serializers import ItemSerializer, OrderSerializer, OrderItemSerializer


class ListItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    
class DetailItemView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    
    
class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
class OrderItemView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    

