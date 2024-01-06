from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from django.forms import ModelForm, Textarea, HiddenInput,DateInput

from .models import Department, Payment, Banking, Expenses, Exp_break, Request, Request_items

class DepartmentForm(forms.ModelForm):
    class Meta:
        model= Department
        fields= '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['receipt_no', 'department', 'client_name', 'contact', 'email',
                  'payment_purpose', 'amount_paid', 'balance', 'recieved_by']

class BankingForm(forms.ModelForm):
    class Meta:
        model = Banking
        fields = ['date', 'department', 'bank_name', 'account_no', 'account_name',
                  'bank_receipt_no', 'amount_banked', 'curency', 'source', 'file', 'banked_by']

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'

class ExpBreakForm(forms.ModelForm):
    class Meta:
        model = Exp_break
        fields ='__all__'

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

class RequestItemsForm(forms.ModelForm):
    class Meta:
        model = Request_items
        fields = ['request', 'item', 'quantity']
        