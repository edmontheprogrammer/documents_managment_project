from django.contrib.auth.decorators import login_required

from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


@login_required
def openAccountFormPage(request):
    return render(request, 'open-account.html', {})


@login_required
def closeAccountFormPage(request):
    return render(request, 'close-account.html', {})
