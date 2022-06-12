from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(required=True, )
    state = forms.CharField()
    delivery_address = forms.CharField()

    class Meta:
        model = User
        fields = ['username',
                'first_name',
                'last_name',
                'state',
                'delivery_address',
                'mobile',
                ]

class UserCreationForm(UserCreationForm):
    mobile = forms.IntegerField(required=True, )
    state = forms.CharField()
    first_name = forms.CharField( required=False)
    last_name = forms.CharField( required=False)
    delivery_address = forms.CharField(help_text='You can add this later')
    email = forms.EmailField( help_text='Enter a valid email address')
    class Meta:
        model= User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'state',
            'delivery_address',
            'mobile',
            'password1',
            'password2',
        ]
        labels = {'mob':'Mobile Number', 'state': 'State of Residence',}
   