from django.urls import path
from .views import (cart_view, delete_order, empty_cart, order_item, order_summary
)

app_name = 'cart' 
urlpatterns = [
path('',cart_view, name='cart'),
path('delete_order/<int:id>', delete_order),
path('clear/', empty_cart),
path('order_summary',order_summary, name='order-summary'),
path('order_item',order_item, name='order-item')

]
