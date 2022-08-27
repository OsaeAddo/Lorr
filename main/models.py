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

#Todo: add stock(quantity) of an item available
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=2)
    label = models.CharField(choices=LABEL, max_length=2)
    description = models.TextField()
    
    
    class Meta:
        verbose_name_plural = "Items"
    
    
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
    
    class Meta:
        verbose_name_plural = "Order Items"
    
    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"
    
    def get_total_item_price(self):
        """
        returns total price of each item.
        e.g 3 orders of a white shirt that costs $20 each will return 
        $60 as the get_total_item_price()

        Returns:
            _type_: float
        """
        return self.item.price * self.quantity
    
    
    
    def get_discount_item_price(self):
        """
        returns the total price of each item with discount applied

        Returns:
            _type_: _float_
        """
        return self.item.discount_price * self.quantity
    
    
    
    def get_total_amount_saved(self):
        """
        returns amount of money customer saves if discount is applied to the item

        Returns:
            _type_: _description_
        """
        return self.get_total_item_price() - self.get_discount_item_price()
    
    
    
    def get_price_used(self):
        """
        returns the final method used to evaluate the price of the item
        i.e if actual price is used or discounted price is used instead.

        Returns:
            _type_: _func_
        """
        if self.item.discount:
            return self.get_discount_item_price()
        
        return self.get_total_item_price()

        
    
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name_plural = "Orders"
    
    
    def __str__(self):
        return self.user.username
    
    
    def get_total_price(self):
        """
        returns the total amount in price of all ordered items
        """
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
            
        return total