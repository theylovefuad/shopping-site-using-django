from random import choices
from django import forms
from .models import Product, Category, HomeSlides

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

INSTRUCTIONS = (
    ('Available','Available'),
    ('Shipped from Abroad', 'Shipped from Abroad'),
    ('Out of Stock','Out of Stock'),
)


class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='Title', widget=forms.TextInput(attrs={
                                                            "placeholder":"Your Title"
                                                }))
    category    = forms.Select(choices=choice_list)
    description = forms.Textarea()
    instruction = forms.Select(choices=INSTRUCTIONS)
    price       = forms.DecimalField(initial=199.99, required=True) 
    class Meta:
        model=Product
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
class SlideForm(forms.ModelForm):
    class Meta:
        model = HomeSlides
        fields = ['image1',
             'image1text',
             'image2',
             'image2text',
             'image3',
             'image3text']       

