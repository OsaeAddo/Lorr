from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.utils import timezone


from .models import Item, Order, OrderItem


class HomeView(ListView):
    model = Item
    template_name = "main/home.html"
    
    
    
class ProductView(DetailView):
    model = Item
    template_name = "main/product.html"
    
    
    
def add_to_cart(request, pk):
    """_summary_
    add a product to OrderItem, and
    add detail order(OrderItem) to Order 
    """
    item = get_object_or_404(Item, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    # if user has Orders
    if order_qs.exists():
        order = order_qs[0]
        
        # if there's an orderitem in the order, increase the quantity by 1
        if order.items.filter(item__pk = item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("core:product", pk=pk)
        # add an orderitem to the order
        else:
            order.items.add(order_item)
            messages.info(request, "Item add to your cart")
            return redirect("core:product", pk=pk)
        
    # if user has no order, create a new order & add an orderitem
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("core:product", pk=pk)
    


def remove_from_cart(request, pk):
    """
    remove all products from OrderItem,
    remove detail order(OrderItem) from Order.

    
    """
    item = get_object_or_404(Item, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    
    #if cart contains an Order
    if order_qs.exists():
        order = order_qs[0]
        
        if order.items.filter(item__pk = item.pk).exists():
            order_item = OrderItem.objects.filter(
                user=request.user,
                item=item,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, f"Item {order_item.item.item_name} removed from your cart")
            return redirect("core:product", pk=pk)
        else:
            messages.info(request, "This item is not in your cart")
            return redirect("core:product", pk=pk)
        
    #if there is no Order in the cart
    else:
        messages.info(request, "You do not have an order")
        return redirect("core:product", pk=pk)