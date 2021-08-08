"""smallbizz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import cart.views as cart_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('pannel/', admin.site.urls),
    path('product/new/',cart_views.add_product.as_view(),name='add-product'),
    path('product/delete/<int:pk>',cart_views.delete_product.as_view(),name='delete-product'),
    path('product/edit/<int:pk>',cart_views.edit_product.as_view(),name='edit-product'),

    path('', include('seller.urls') ), #should always stay at end
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
