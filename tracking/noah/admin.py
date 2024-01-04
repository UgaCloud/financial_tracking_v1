from django.contrib import admin

# Register your models here.

# tourism_app/admin.py
from django.contrib import admin
from .models import Department, Payment, Banking, Expenses, Exp_break, Request, Request_items

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
admin.site.register(Department, DepartmentAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display=('date_paid', 'receipt_no', 'department', 'client_name', 'contact', 'email', 'payment_purpose', 'amount_paid', 'balance', 'recieved_by')
admin.site.register(Payment, PaymentAdmin)


class BankingAdmin(admin.ModelAdmin):
    list_display =('date', 'department', 'bank_name', 'account_no', 'bank_receipt_no', 'amount_banked', 'curency', 'source', 'file', 'banked_by')
admin.site.register(Banking, BankingAdmin)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('expense_date', 'department', 'purpose', 'amount_recieved', 'spent_by', 'date_recieved')
admin.site.register(Expenses,ExpensesAdmin)


class Exp_breakAdmin(admin.ModelAdmin):
    list_display = ('expense', 'particular', 'rate', 'quantity')
admin.site.register(Exp_break, Exp_breakAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_date', 'requested_by', 'purpose', )
admin.site.register(Request, RequestAdmin)


class Request_itemsAdmin(admin.ModelAdmin):
    list_display = ('request', 'item', 'quantity')
admin.site.register(Request_items, Request_itemsAdmin)
