from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, SellerUpdateForm, PinUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Seller, SellerInavailability
from django.contrib.auth.models import User
import requests
from cart.models import Category, Product, Order, OrderItem, Reviews
from django.views.generic import (ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse

blacklist=[
    'accounts',
    'pannel',
]


class add_inavailability (LoginRequiredMixin, CreateView):
    model = SellerInavailability
    fields = ['date_unavailable']

    def form_valid(self,form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)
    def get_success_url(self,**kwargs):
        return reverse('profile',args = (self.request.user.username,))

class edit_inavailability (LoginRequiredMixin, UpdateView):
    model = SellerInavailability
    fields = ['date_unavailable']

    def form_valid(self,form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)
    def get_success_url(self,**kwargs):
        return reverse('profile',args = (self.request.user.username,))

class delete_inavailability (LoginRequiredMixin, DeleteView):
    model = SellerInavailability

    def get_success_url(self,**kwargs):
        return reverse('profile',args = (self.request.user.username,))


def homepage(request):
    return render (request,'seller/homepage.html')

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            if username not in blacklist :
                form.save()
                messages.success(request, f'Your account has been created! You are now able to log in')
                
                return redirect('login')
            else:
                messages.warning(request, f'Please Enter a valid username')
                form = UserRegisterForm()
    else:
        form = UserRegisterForm()
    return render(request, 'seller/register.html', {'form': form})

def login_redirect(request):
    return redirect('profile',request.user.username)

def profile(request,uname):
    Authenticated = True if request.user.username==uname else False
    try:
        owner = User.objects.get(username=uname)
        seller = Seller.objects.get(Owner=owner)
        context={
        'Authenticated' :   Authenticated,
        'owner'          :   owner,
        'seller'        :   seller,
        }
        try:
            products = Product.objects.filter(seller=seller)
            context['products'] =  products
        except Exception as e:
            print(e)
            print("no products found")
        try:
            dates_unavailable = SellerInavailability.objects.filter(seller=seller)
            context['dates_unavailable'] = dates_unavailable
        except Exception as e:
            print(e)
            print("no dates found")
        if seller.StoreName:
            return render(request, 'seller/profile.html', context)
        else:
            messages.warning(request,f'Please Complete your Profile')
            return redirect('edit-profile')
    except Exception as e:
        print(e)
        print("render-error")
        return render(request, 'seller/profile_error.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        s_form = SellerUpdateForm(  request.POST,
                                    request.FILES,
                                    instance=request.user.seller)
        if u_form.is_valid() and s_form.is_valid():
            u_form.save()
            s_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile',request.user.username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        s_form = SellerUpdateForm(instance=request.user.seller)

    context = {
        'u_form': u_form,
        's_form': s_form,
    }

    return render(request, 'seller/profile-edit.html', context)

@login_required
@csrf_exempt
def edit_pin(request):
    Object_pin = request.user.seller.pincode
    if request.method=='POST':
        pin_form = PinUpdateForm(request.POST,instance=request.user.seller)
        if pin_form.is_valid():
            Obj = pin_form.save(commit=False)
            if Obj.pincode.isdigit():
                messages.success(request, f'Your account has been updated!')
                return redirect('profile',request.user.username)
            else:
                pin_form = PinUpdateForm(instance=request.user.seller)
                context={
                    'pin_form':pin_form,
                    'current_pin': Object_pin,
                }
                return render(request,'seller/profile-edit-pin.html',context)

    else:
        pin_form = PinUpdateForm(instance=request.user.seller)
    context={
        'pin_form':pin_form,
        'current_pin': Object_pin,
    }
    return render(request,'seller/profile-edit-pin.html',context)

@login_required
def edit_latlong(request,placename,pincode):
    User=request.user
    if placename:
        placename.split('-')
        search=""
        Iter=0
        for place in placename.split('-'):
            search+=place
            Iter+=1
            if Iter!=3:
                search+="/"
        url = 'https://nominatim.openstreetmap.org/search/' + search +'?format=json'
        response_=requests.get(url)
        response = response_.json()
        if response:
            User.seller.latitude=response[0]['lat']
            User.seller.longitude=response[0]['lon']
            User.seller.pincode=pincode
            User.seller.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile',request.user.username)
        else:
            messages.warning(request, f'Couldn\'t find resources to locate you, Please Select Another Option')
    return redirect('edit-pin')
