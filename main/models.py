from unicodedata import category
from django.db import models
from django.conf import settings
from django.shortcuts import reverse


CATEGORY = (
    ('S', 'Shirt'),
    ('SP', 'Sport Wear'),
    ('OW', 'Out Wear')
)


LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller')
)


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=LABEL, max_length=2)
    label = models.CharField(choices=LABEL, max_length=2)
    description = models.TextField()
    
    
    def __str__(self):
        return self.item_name
    
    
    def get_absolute_url(self):
        return reverse(
            "core: product", 
            kwargs = {
                "pk": self.pk
            }
        )
        
    
    def get_add_to_cart_url(self):
        return reverse(
            "core: add-to-cart",
            kwargs = {
                "pk": self.pk
            }
        )
        
        
    def get_remove_from_cart_url(self):
        return reverse(
            "core: remove-from-cart",
            kwargs = {
                "pk": self.pk
            }
        )
        


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"
    
    def get_total_item_price(self):
        """
        return total price of each item.
        e.g 3 orders of a white shirt that costs $20 each will return 
        $60 as the get_total_item_price()

        Returns:
            _type_: float
        """
        return self.item.price * self.quantity
    
    
    
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.user.username