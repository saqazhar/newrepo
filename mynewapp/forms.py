from django import forms
from .models import myform

class myformForm(forms.ModelForm):

    class meta:
        model = myform
        fields = ('name', 'email')