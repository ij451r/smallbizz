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
from django.urls import path
from . import views as seller_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', seller_views.homepage,name='homepage'),
    path('accounts/register/',seller_views.register,name='register'),

    path('accounts/login/',auth_views.LoginView.as_view(template_name ='seller/login.html'), name= 'login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(template_name='seller/logout.html'), name= 'logout'),

    path('accounts/pass-reset/',
        auth_views.PasswordResetView.as_view(template_name='seller/password_reset.html'),
        name = 'password-reset'
        ),
    path('accounts/pass-reset-done/',
        auth_views.PasswordResetDoneView.as_view(template_name='seller/password_reset_done.html'),
        name = 'password_reset_done'
        ),
    path('accounts/pass-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='seller/password_reset_confirm.html'),
        name = 'password_reset_confirm'
        ),
    path('accounts/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='seller/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('accounts/login-redirect/',seller_views.login_redirect,name='login-redirect'),
    path('accounts/edit/',seller_views.edit_profile,name='edit-profile'),
    path('accounts/edit/pin/',seller_views.edit_pin,name='edit-pin'),
    path('accounts/edit/pin/<placename>/<int:pincode>',seller_views.edit_latlong,name='edit-latlong'),
    path('accounts/inavailability',seller_views.add_inavailability.as_view(),name='add-inavailability'),
    path('accounts/inavailability/delete/<int:pk>',seller_views.delete_inavailability.as_view(),name='delete-inavailability'),
    path('accounts/inavailability/edit/<int:pk>',seller_views.edit_inavailability.as_view(),name='edit-inavailability'),

    path('<uname>/',seller_views.profile, name = 'profile'), #always should stay at the end
]
'''path('delete/<int:pk>/',
    seller_views.UserDeleteView.as_view(template_name='users/user_confirm_delete.html'),
    name = 'delete'
    ),'''
