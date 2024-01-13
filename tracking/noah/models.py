from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required


# Create your models here.
# @staff_member_required(login_url='signup')
# @login_required(login_url='login')
# @user_passes_test(lambda u: u.is_staff, login_url='signup')
# @user_passes_test(lambda u: u.is_superuser, login_url='signup')
# @user_passes_test(lambda u: u.groups.filter(name='department').exists(),login_url='login')  
class Department(models.Model):
    name = models.CharField(verbose_name='Department Name',max_length=50)
    description = models.TextField(max_length=50,null=True,blank=True)
    price = models.IntegerField()
    

    class Meta:
        verbose_name=('Department')
        verbose_name_plural=('Departments')

    def __str__(self):
        return self.name

        
        

class Payment(models.Model):
    date_paid =models.DateField(auto_now=True)
    receipt_no = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete= models.CASCADE,related_name='Department')
    client_name = models.CharField(max_length=50)
    contact= models.CharField(max_length=50)
    email = models.EmailField()
    payment_purpose = models.CharField(max_length=50)
    amount_paid = models.IntegerField()
    balance =models.IntegerField()
    recieved_by = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name=('Payment')
        verbose_name_plural=('Payments')

    def __str__(self):
        return self.payment_purpose

        

class Banking(models.Model):
    date = models.DateField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department')
    bank_name =models.CharField(max_length=50)
    account_no= models.CharField(max_length=50)
    account_name=models.CharField(max_length=50)
    bank_receipt_no= models.CharField(max_length=50)
    amount_banked = models.IntegerField()
    curency= models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    file=models.FileField()
    banked_by=models.CharField(max_length=50)

    class Meta:
        verbose_name=('Banking')
        verbose_name_plural=('Bankings')

    def __str__(self):
        return self.account_no

        
        
class Expenses(models.Model):
    expense_date= models.DateField(auto_now=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,verbose_name='department')
    purpose=models.CharField(max_length=50)
    amount_recieved= models.IntegerField()
    # attachment
    spent_by=models.CharField(max_length=50)
    date_recieved=models.DateField()

    class Meta:
        verbose_name=('Expense')
        verbose_name_plural=('Expenses')

    def __str__(self):
        return f"{self.expense_date} - {self.department} - {self.purpose}"

        

class Exp_break(models.Model):
    expense=models.ForeignKey(Expenses,on_delete=models.CASCADE,verbose_name='expense')
    particular=models.CharField(max_length=50)
    rate= models.CharField(max_length=50)
    quantity=models.IntegerField()

    class Meta:
        verbose_name=('Exp_break')
        verbose_name_plural=('Exp_breaks')

    def __str__(self):
        return self.particular

        

class Request(models.Model):
    request_date = models.DateField(auto_now=True)
    requested_by = models.CharField(max_length=50)
    purpose= models.CharField(max_length=50)

    class Meta:
        verbose_name=('Request')
        verbose_name_plural=('Requests')

    def __str__(self):
        return self.purpose

     

class Request_items(models.Model):
    request= models.ForeignKey(Request,on_delete=models.CASCADE,verbose_name='request')
    item= models.CharField(max_length=50)
    quantity= models.IntegerField()

    class Meta:
        verbose_name=('Request_item')
        verbose_name_plural=('Request_items')

    def __str__(self):
        return self.particular

       


    

