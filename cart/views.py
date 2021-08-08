from django.shortcuts import render
from .models import Category, Product, Order, OrderItem, Reviews
from django.views.generic import (ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse



class add_product (LoginRequiredMixin, CreateView):
    model = Product
    fields = ['category', 'Product_Name', 'Product_Description','Product_Image_1','Product_Image_2']

    def form_valid(self,form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)
    def get_success_url(self,**kwargs):
        return reverse('profile',args = (self.request.user.username,))


class delete_product (UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Product

    def test_func(self):
        Obj = self.get_object()
        if self.request.user.seller == Obj.seller :
            return True
        False

    def get_success_url(self,**kwargs):
        return reverse('profile',args = (self.request.user.username,))

class edit_product (LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['category', 'Product_Name', 'Product_Description','Product_Image_1','Product_Image_2']

    def form_valid(self,form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)

    def get_success_url(self,**kwargs):
        return reverse('profile',args = (self.request.user.username,))
