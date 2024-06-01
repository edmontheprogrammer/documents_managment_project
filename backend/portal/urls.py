from django.urls import path, include
from . import views

urlpatterns = [
    # This includes all of the built-in URLs from allauth:
    path("accounts/", include("allauth.urls")),
    # This line should send the users to the "account_login" page
    # "accounts/login"
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signin-page/', views.signinpage, name='signin-page'),
    path('create-account-page/', views.createaccountpage,
         name='create-account-page'),
]
