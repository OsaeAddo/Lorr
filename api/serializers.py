from rest_framework import serializers


from main.models import Item, Order, OrderItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'item_name', 'price', 'discount_price', 
            'category', 'label', 'description'
        )
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'user', 'items',
            'start_date', 'ordered_date', 'ordered'
        )
        

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'user', 'item',
            'ordered', 'quantity'
        )
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')