
from django.urls import path, include
from . import views

urlpatterns = [
    # This includes all of the built-in URLs from allauth:
    # This is basically placing all of the Django authenticaiton
    # built-in URLs and allauth URLs into the sub URLS of "accounts/"
    # path("accounts/", include("allauth.urls")),
    # For example, this line should send the users to the "account_login" page
    # "accounts/login"
    # Note 1: You must have Django allauth at the top of the urlpatterns
    #
    # Note 2: "Django allauth" does a catch all for all of the URL patterns that
    # gets send by the web client and it goes through all of the built-in URLs
    # (login, signup, password_reset, email and others) and it tries to
    # render one of them. If Django allauth didn't find the URL then it goes to
    # the bottom of the urlpatterns and such as
    #  " path('', views.home, name='home'),  "
    #  " path('about/', views.about, name='about'), "
    #  " path('contact/', views.contact, name='contact'), "
    path("", include("allauth.urls")),
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('open-account-form-page/', views.openAccountFormPage,
         name='open-account-form-page'),
    path('open-account-form-page/<int:pk>', views.edit_openAccountFormPage,
         name='edit-open-account-form-page'),


    path('close-account-form-page/', views.closeAccountFormPage,
         name='close-account-form-page'),


]
