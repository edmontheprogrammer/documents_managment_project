from django import forms
from .models import Telecommunications


class TelecommunicationsForm(forms.ModelForm):
    # 1. photo field
    government_id_photo = forms.ImageField()
    # 2. documents upload filed 1
    # 3. documents upload filed 2
    # 4. user hand signature field
    #

    class Meta:
        model = Telecommunications
        fields = '__all__'
        # Labels for writing different field names than what's already named
        # on the model fields "labels" will overwrite what's already generated by
        # model form
        labels = {

        }