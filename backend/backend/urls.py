"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from portal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Notes on allauths URLs:
    # The links "/accounts/login/", "/accounts/signup/", are publically accessiable
    # The links "/accounts/logout/",
    # Password Management links ("account_email", "account_email") are private and requires users authentications
    # for new users to have access to it.
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name="profile"),

    # URL for the django REST framework
    # path('api-auth/', include('rest_framework.urls')),
    # URL for the django-rest-authtoken
    # path('auth/', include('rest_authtoken.urls')),
]
