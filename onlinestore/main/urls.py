from django.urls import path
from .views import (
                   product_view,
                   product_detail,
                   add_reviews,
)

app_name = 'product' #namespacing
urlpatterns = [
path('all/', product_view, name='all-products'),
path('<str:pk>/',product_detail, name='product_detail'),   
path('<str:pk>/review',add_reviews), 

]
