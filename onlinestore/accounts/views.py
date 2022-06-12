from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, UpdateUserForm
from django.contrib import messages
from main.models import HomeSlides



def login_view(request):
    queryset = HomeSlides.objects.get(id=1)
    context = {'image':queryset}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username,
                            password=password)
        if user is None:
            context = {"error":"Invalid username or password"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect('product:all-products')
    return render(request, "accounts/login.html", context)

def signup_view(request):
        form= UserCreationForm(request.POST or None)
        if form.is_valid():
            user_obj=form.save()
            return redirect ('/accounts/login')
        context = {"form":form}
        return render (request, "accounts/signup.html",context)

def logout_view(request):
        if request.method == 'POST':
                logout(request)
        return render(request,"accounts/logout.html")

from django.shortcuts import render

def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user-update')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'accounts/user_update.html', {'user_form': user_form})# Create your views here.
