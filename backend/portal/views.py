from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .forms import TelecommunicationsForm


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


# @login_required
def openAccountFormPage(request):
    if request.method == "POST":
        filled_form = TelecommunicationsForm(request.POST, request.FILES)
        if filled_form.is_valid():
            note = "Thanks for completing the application form for opening an account with us. Our team is processing your request! DMP Team"
            new_form = TelecommunicationsForm()
            return render(request, "open-account.html", {"telecommunicationsform": new_form, 'note': note})
    else:
        form = TelecommunicationsForm()
        return render(request, 'open-account.html', {'telecommunicationsform': form})


@login_required
def closeAccountFormPage(request):
    return render(request, 'close-account.html', {})
