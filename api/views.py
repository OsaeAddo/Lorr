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
    
    

#for admin only
class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
class DetailOrderView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer




    
#<-------- for both admin(read-only) & customers(read-write)
class OrderItemView(generics.ListAPIView):
    """
    Display all ordered items
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    
class DetailOrderItemView(generics.RetrieveAPIView):
    """
    Display each ordered item
    """ 
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    


