from django.shortcuts import render
from django.contrib.auth import get_user_model


from rest_framework import generics, viewsets

from main.models import Item, Order, OrderItem

from .serializers import ItemSerializer, OrderSerializer, OrderItemSerializer, UserSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    #retrieve a user's ip address
    def user_ip_address(self, request):
        ip_addr = request.META['REMOTE_ADDR']
        return ip_addr
        
    
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    

#for admin only
class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderDetailView(generics.RetrieveAPIView):
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
    
    


