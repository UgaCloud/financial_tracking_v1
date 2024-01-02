from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from django.forms import ModelForm, Textarea, HiddenInput,DateInput

from .models import Department

class Department_Form(forms.ModelForm):
    class Meta:
        Model= Department
        fields= '__all__'
        