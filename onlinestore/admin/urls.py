from django.urls import path

from .views import (ProductCreateView,
                    ProductUpdateView,
                    pending_orders,
                    admin_dashboard,
                    admin_view,
                    product_view,
                    product_detail,
                    update_status,
                    HomeSlideCreateView
)

app_name = 'bld_admin' #namespacing
urlpatterns = [
path('create/',ProductCreateView.as_view(), name = 'create'),
path('slides/', HomeSlideCreateView.as_view()),
path('',admin_dashboard),
path('allproducts/', product_view, name ='allproducts'),
path('product/<str:pk>/update', ProductUpdateView.as_view(),),
path('product/<str:pk>/',product_detail),
path('completed_orders/', admin_view, name='admin_view'),
path('pending_orders/', pending_orders, name='pending_orders'),
path('update_status/<int:id>/', update_status, name='update_status')
]

