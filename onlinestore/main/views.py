from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm
from .models import Product, Category, Reviews, Order, HomeSlides
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from accounts.models import Profile


# Create your views here.

def home_view(request):
    queryset = HomeSlides.objects.get(id=1)
    context = {'image':queryset}
    return render (request, "main/home.html", context)

def product_view(request):
    queryset= Product.objects.all() 
    queryset2= Category.objects.all()
    context= {
                "object_list":queryset,
                "category_list":queryset2
    }
    return render (request, "main/product_view.html", context)

def category_view(request, cats):
    queryset= Product.objects.filter(category=cats)
    queryset2= Category.objects.all()
    context = {
        'cats':cats,
        'object_list': queryset,
        "category_list":queryset2
    }
    return render(request, 'categories.html', context)

def product_detail(request, pk):
    queryset=Reviews.objects.filter(product=Product.objects.get(pk=pk))
    if request.method == "POST":        
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        Order.objects.create(user=request.user, title=title, price=price, quantity=quantity)
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    context={
        "object": obj,
        "review":queryset
    } 
    return render (request, "main/product_detail.html", context)

def add_reviews(request, pk):
    if request.method == "POST":
        user = request.user
        product = Product.objects.get(pk=pk)
        review = request.POST.get("review")

        reviews = Reviews.objects.create(user=user, product=product, review=review, )
        reviews.save()
        messages.success(request, "Thank You for Reviewing this Item!!")
    return render (request, "main/review.html",{})



def search_view(request):
    if request.method=="POST":
        searched = request.POST.get('searched')
        queryset= Product.objects.filter(title__contains=searched)
        context={'searched':searched,
                 'items':queryset}
        return render(request, 'main/search.html', context)
    else:
        return render(request, 'main/search.html',context)


@login_required(login_url='/accounts/login/')
def admin_view(request):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    cart_items = Order.objects.filter(ordered=True,status="Delivered").order_by('-ordered_on')
    context = {
        'cart_items':cart_items,
    }
    return render(request, 'admin/admin_view.html', context)

@login_required
def update_status(request, id):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    if request.method == 'POST':
        status = request.POST['status']
    cart_items = Order.objects.filter(user=request.user, ordered=True,status="Active",id=id)
    delivery_date = timezone.now()
    if status == 'Delivered':
        cart_items.update(status=status)
    return render(request, 'admin/pending_orders.html')

@login_required(login_url='/accounts/login/')
def pending_orders(request):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    items = Order.objects.filter(user=request.user, ordered=True,status="Active").order_by('-ordered_on')
    context = {
        'items':items,
    }
    return render(request, 'admin/pending_orders.html', context)

@login_required(login_url='/accounts/login/')
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    cart_items = Order.objects.filter(user=request.user, ordered=True)
    pending_total = Order.objects.filter(user=request.user, ordered=True,status="Active").count()
    completed_total = Order.objects.filter(user=request.user, ordered=True,status="Delivered").count()
    count1 = Order.objects.filter(user=request.user, ordered=True).count()
    count2 = Order.objects.filter(user=request.user, ordered=True).count()
    count3 = Order.objects.filter(user=request.user, ordered=True).count()
    total = Order.objects.filter(user=request.user, ordered=True).aggregate(Sum('price'))
    income = total.get("price__sum")
    context = {
        'pending_total' : pending_total,
        'completed_total' : completed_total,
        'income' : income,
        'count1' : count1,
        'count2' : count2,
        'count3' : count3,
    }
    return render(request, 'admin/admin_dashboard.html', context)
