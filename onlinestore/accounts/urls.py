from django.urls import path
from .views import (login_view, logout_view, signup_view, profile)


app_name = 'accounts' #namespacing
urlpatterns = [
path('signup/',signup_view,),
path('login/',login_view,),
path('logout/',logout_view),
path('user/',profile, name='user-update') 
]
