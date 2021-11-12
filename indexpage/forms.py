from django import forms
#from django import ModelForm
from .models import Appoinment

class AppoinmentForms(forms.Form):
        class Meta:
                model = Appoinment
                flelds = ('name','email','department')