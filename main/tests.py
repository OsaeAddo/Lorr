from django.test import TestCase

from .models import Item


class ItemTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Item.objects.create(
            item_name="Lorr-test-shirt", price=22, discount_price=0,
            category="Shirt", label="N", description="Create test shirt"
        )
        
        
    def test_item_name(self):
        item = Item.objects.get(id=1)
        expected_item_name = f'{item.item_name}'
        self.assertEquals(expected_item_name, 'Lorr-test-shirt')
        
        
    def test_item_price(self):
        item = Item.objects.get(id=1)
        expected_item_price = item.price
        self.assertEquals(expected_item_price, 22)
        
        
    
    def test_item_discount_price(self):
        item = Item.objects.get(id=1)
        expected_item_discount_price = item.discount_price
        self.assertEquals(expected_item_discount_price, 0)
        
        
    def test_item_category(self):
        item = Item.objects.get(id=1)
        expected_item_category = f'{item.category}'
        self.assertEquals(expected_item_category, 'Shirt')
        
        
    
    def test_item_label(self):
        item = Item.objects.get(id=1)
        expected_item_label = f'{item.label}'
        self.assertEquals(expected_item_label, 'N')
        
        
        
    def test_item_description(self):
        item = Item.objects.get(id=1)
        expected_item_description = f'{item.description}'
        self.assertEquals(expected_item_description, 'Create test shirt')
        
        