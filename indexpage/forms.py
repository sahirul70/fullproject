from django import forms
from django.forms import ModelForm
from .models import Appointment,Contact,Commant

class AppointmentForm(forms.ModelForm):
        class Meta:
                model = Appointment
                fields =['name','email','subject']

class ContactForm(forms.ModelForm):
        class Meta:
                model = Contact
                fields =['name','email','subject','massage']
class CommantForm(forms.ModelForm):
        class Meta:
                model = Commant
                fields =['name','email','body']