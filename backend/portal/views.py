
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def signinpage(request):
    return render(request, 'signin.html', {})


def createaccountpage(request):
    return render(request, 'createaccount.html', {})
