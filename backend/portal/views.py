from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .forms import TelecommunicationsForm

from .models import Telecommunications


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


# @login_required
def openAccountFormPage(request):
    if request.method == "POST":
        # Note 1: "request.FILES" is needed in this method because that's how we allow
        # our form to accept user uploaded files such as "images", "PDFs", and "word documents"
        filled_form = TelecommunicationsForm(request.POST, request.FILES)
        if filled_form.is_valid():
            # This line is saving the Model Form into the database: "filled_form.save()"
            created_telecommunications = filled_form.save()
            created_telecommunications_pk = created_telecommunications.id
            note = "Thanks %s %s for completing the application form for opening an account with us. Our team is processing your request! DMP Team" % (
                filled_form.cleaned_data['first_name'], filled_form.cleaned_data['last_name'],)
            filled_form = TelecommunicationsForm()
        else:
            note = "New Account Application Form has failed. Try again."
            created_telecommunications_pk = None


        return render(request, "open-account.html", {'created_telecommunications_pk': created_telecommunications_pk,
                                                     "telecommunicationsform": filled_form,
                                                     'note': note})
    else:
        form = TelecommunicationsForm()
        return render(request, 'open-account.html', {'telecommunicationsform': form})


def edit_openAccountFormPage(request, pk):
    telecommunications = Telecommunications.objects.get(pk=pk)
    form = TelecommunicationsForm(instance=telecommunications)
    if request.method == 'POST':
        filled_form = TelecommunicationsForm(
            request.POST, instance=telecommunications)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = "New Account Form has been updated"
            return render(
                request,
                'edit-open-account.html',
                {'note': note,
                 'telecommunicationsform': form,
                 'telecommunications': telecommunications}
            )
    return render(
        request,
        'edit-open-account.html',
        {'telecommunicationsform': form, 'telecommunications': telecommunications}
    )


@login_required
def closeAccountFormPage(request):
    return render(request, 'close-account.html', {})
