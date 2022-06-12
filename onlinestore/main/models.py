from doctest import DONT_ACCEPT_TRUE_FOR_1
from django.utils import timezone
from django.db import models
from accounts.forms import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    INSTRUCTIONS = (
        ('Available', 'Available'),
        ('Out of Stock', 'Out of Stock'),
        ('Shipped from Abroad', 'Shipped from Abroad')
    )   
    choices = Category.objects.all().values_list('name','name')
    choice_list = []
    for item in choices:
        choice_list.append(item)

                
    title = models.CharField(max_length=60, primary_key=True, unique=True)
    price= models.FloatField(default=100.00)
    category= models.CharField(max_length=100, choices=choice_list)
    description= models.CharField(max_length=250, blank=True, null= True)
    instructions= models.CharField(max_length=100, choices= INSTRUCTIONS)
    image= models.ImageField(upload_to='images')
    image2= models.ImageField(upload_to='images',blank=True, null= True)
    image3= models.ImageField(upload_to='images',blank=True, null= True)

    

    def __str__(self):
        return self.title +  '|'  + self.category

    class Meta:
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse ('product:product_detail', args=(str(self.pk)))

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    review = models.TextField()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review

class Order(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Delivered', 'Delivered')
    )

    model = Product
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    sesh   = models.CharField(max_length=255, default='01')
    title = models.CharField(max_length=150)
    price = models.FloatField()
    quantity = models.IntegerField()
    ordered_on = models.TimeField(default=timezone.now)
    ordered = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Active')

class HomeSlides(models.Model):
    image1 = models.ImageField(upload_to='images')
    image1text = models.CharField(max_length=10000, default='')
    image2 = models.ImageField(upload_to='images')
    image2text = models.CharField(max_length=10000, default='')
    image3 = models.ImageField(upload_to='images')
    image3text = models.CharField(max_length=10000, default='')



