from django.shortcuts import render, redirect
from django.db.models import Sum, F
from main.models import Order
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def cart_view(request):
    queryset = Order.objects.filter(user=request.user,ordered=False) 
    queryset = queryset.annotate(total_value=F('quantity') * F('price'))
    bill = queryset.aggregate(Sum('total_value'))
    pieces = queryset.aggregate(Sum('quantity'))
    total = bill.get("total_value__sum")
    total_pieces = pieces.get("quantity__sum")
    context = {
        'object_list':queryset,
        'total': total,
        'total_pieces': total_pieces,
    }
    return render (request, "order/cart.html",context)


  

def delete_order(request, id,):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('cart:cart')

def empty_cart(request):
    queryset=Order.objects.filter(user=request.user)
    queryset.delete()
    return redirect('cart:cart')

def order_item(request):
    cart_items = Order.objects.filter(user=request.user,ordered=False)
    ordered_on=timezone.now()
    cart_items.update(ordered=True,ordered_on=ordered_on,status='Active')
    messages.info(request, "Item Ordered")
    return redirect('cart:order-summary')

def order_summary(request):
    queryset = Order.objects.filter(user=request.user, ordered=True,status="Active").order_by('-ordered_on')
    cart_items = Order.objects.filter(user=request.user, ordered=True,status="Delivered").order_by('-ordered_on')
    bill = cart_items.aggregate(Sum('price'))
    pieces = cart_items.aggregate(Sum('quantity'))
    total = bill.get("price__sum")
    total_pieces = pieces.get("quantity__sum")
    context = {
        'object_list':queryset,
        'cart_items':cart_items,
        'total': total,
        'total_pieces': total_pieces,
    }
    return render(request, 'order/order_summary.html', context)

   

