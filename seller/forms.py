from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Seller

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class SellerUpdateForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'StoreName',
            'StoreLogo',
            'phone_number',
            'Deliver_anywhere',
            'Local_Delivery_Distance',
            'insta_social',
            ]

class PinUpdateForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields=[
            'pincode',
        ]
