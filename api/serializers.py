from rest_framework import serializers


from main.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'item_name', 'price', 'discount_price', 
            'category', 'label', 'description'
        )
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user', 'item',
            'ordered', 'quantity'
        )
        
