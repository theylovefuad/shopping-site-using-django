"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from main.views import (category_view, search_view, home_view)


urlpatterns = [
    path('',home_view),
    path('admin/', admin.site.urls),
    path('bld_admin/', include('admin.urls')),
    path('product/', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('order.urls')),
    path('category/<str:cats>/',category_view, name='category'),
    path('search/', search_view, name= 'search')  

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
