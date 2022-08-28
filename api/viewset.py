from rest_framework import viewsets, generics

from main.models import Item, Order, OrderItem

from .serializers import ItemSerializer, OrderSerializer, OrderItemSerializer



class ProductViewSet(viewsets.ModelViewSet):
    #add permission classes
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    


    
    
    
