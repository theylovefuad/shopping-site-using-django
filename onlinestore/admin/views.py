from urllib import request
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from django.http import Http404, HttpResponse
from main.models import Order, Reviews
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from main.forms import ProductForm, SlideForm
from main.models import Product, HomeSlides

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
    total = Order.objects.filter(user=request.user, ordered=True, status = "Delivered").aggregate(Sum('price'))
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

class ProductCreateView(CreateView):
    template_name='admin/product_create.html'
    form_class= ProductForm
    queryset= Product.objects.all()
    success_url = '/bld_admin'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    fields=[
             'title',
             'category',
             'description',
             'instructions',
             'price', 
             'image',
             'image2',
             'image3'
         ]
    template_name = 'admin/product_update.html' # templete for updating
    success_url="/bld_admin/allproducts" # posts list url

def product_view(request):
    if not request.user.is_superuser:
        return HttpResponse(status=403)
    queryset= Product.objects.all() 
    context= {
                "object_list":queryset
    }
    return render (request, "admin/product_view.html", context)

def product_detail(request, pk):
    queryset = Reviews.objects.filter(product=Product.objects.get(pk=pk))

    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    context={
        "review":queryset,
        "object": obj
    } 
    return render (request, "admin/product_detail.html", context)

class HomeSlideCreateView(CreateView):
    template_name='admin/homeslide_create.html'
    form_class= SlideForm
    queryset= HomeSlides.objects.all()
    success_url = '/bld_admin'

