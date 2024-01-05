from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Department, Payment, Banking, Expenses, Exp_break, Request, Request_items
from .forms import DepartmentForm, PaymentForm, BankingForm, ExpensesForm, ExpBreakForm, RequestForm, RequestItemsForm

def IndexView(request):
    return render(request, 'index.html')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def create_department_view(request):
    if request.method == "POST":
        dpt_form = DepartmentForm(request.POST)

        if dpt_form.is_valid():
            dpt_form.save()

    else:
        dpt_form = DepartmentForm()
    department = Department.objects.all()

    context = {
        'form': dpt_form,
        'departments': department
    }
    return render(request, template_name='department_details.html', context=context)




def department_update(request, dpt_id):
    department = Department.objects.get(id=dpt_id)
    form = DepartmentForm(instance=department)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
           form.save()
        return redirect('department-list')
    else:
       form = DepartmentForm(instance=department)
        
    context = {'form': form}
    return render(request, 'department_update.html', context) 


def payment_create(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('payment-list')
    
    context = {'form': form}
    return render(request, 'payment.html', context)



def payment_update(request, pk):
  payment = Payment.objects.get(id=pk)
  form = PaymentForm(instance=payment)

  if request.method == 'POST':
     form = PaymentForm(request.POST, instance=payment)
     if form.is_valid():
       form.save()
       return redirect('payment-list')

  context = {'form': form}
  return render(request, 'payment_update.html', context)


def banking_create(request):
  if request.method == 'POST':
    bank_form = BankingForm(request.POST)
    if bank_form.is_valid():
       bank_form.save()
       
  else:
     bank_form =BankingForm()
  bank =Banking.objects.all()

  context = {
     'form': bank_form,
     'bank': bank}
  return render(request, 'banking.html', context)


def banking_update(request, pk):
  banking = Banking.objects.get(id=pk)
  form = BankingForm(instance=banking)

  if request.method == 'POST':
     form = BankingForm(request.POST, instance=banking)
     if form.is_valid():
       form.save()
       return redirect('payment-list')

  context = {'form': form}
  return render(request, 'payment_update.html', context)



def expense_create(request):
  if request.method == 'POST':
    expense_form = ExpensesForm(request.POST)
    if expense_form.is_valid():
       expense_form.save()
       
  else:
       expense_form = ExpensesForm()
  expense = Expenses.objects.all()

     
  context = {'form': expense_form,
             'expenses':expense}
  return render(request, 'expenses.html', context)



def expense_update(request, pk):
  expense = Expenses.objects.get(id=pk)
  form = ExpensesForm(instance=expense)

  if request.method == 'POST':
     form = ExpensesForm(request.POST, instance=expense)
     if form.is_valid():
       form.save()
       return redirect('expense-list')

  context = {'form': form}
  return render(request, 'expense_update.html', context)


def expBreak_create(request):
  if request.method == 'POST':
    exp_form = ExpBreakForm(request.POST)
    if exp_form.is_valid():
       exp_form.save()
  else:
     exp_form =ExpBreakForm()
  expbreak =Exp_break.objects.all()

  context = {'form': exp_form,
             'expbreak': expbreak}
  return render(request, 'exp_break.html', context)


def expbreak_update(request, pk):
  expbreak = Exp_break.objects.get(id=pk)
  form =ExpBreakForm(instance=expbreak)

  if request.method == 'POST':
     form = ExpBreakForm(request.POST, instance=expbreak)
     if form.is_valid():
       form.save()
       return redirect('expense-list')

  context = {'form': form}
  return render(request, 'expense_update.html', context)



def create_request_view(request):
    if request.method == "POST":
        rqst_form = RequestForm(request.POST)

        if rqst_form.is_valid():
            rqst_form.save()

    else:
        rqst_form = RequestForm()
    requests = Request.objects.all()

    context = {
        'form': rqst_form,
        'requests': requests
    }
    return render(request, template_name='request.html', context=context)


def request_update(request, pk):
    requests = Request.objects.get(id=pk)
    rqt_form = RequestForm(instance=requests)

    if request.method == 'POST':
        rqt_form = RequestForm(request.POST, instance=requests)
        if rqt_form.is_valid():
           rqt_form.save()
        return redirect('department-list')
    else:
       rqt_form = RequestForm(instance=requests)
        
    context = {'form': rqt_form,
               'request': requests}
    return render(request, 'request_update.html', context) 


def create_request_item_view(request):
    if request.method == "POST":
        item_form = RequestItemsForm(request.POST)

        if item_form.is_valid():
            item_form.save()

    else:
        item_form = RequestItemsForm()
    items = Request_items.objects.all()

    context = {
        'form': item_form,
        'item_request': items
    }
    return render(request, template_name='items.html', context=context)


def item_request_update(request, pk):
    item = Request_items.objects.get(id=pk)
    rqt_form = RequestItemsForm(instance=item)

    if request.method == 'POST':
        rqt_item_form = RequestItemsForm(request.POST, instance=item)
        if rqt_item_form.is_valid():
           rqt_item_form.save()
        return redirect('department-list')
    else:
       rqt_form = RequestItemsForm(instance=item)
        
    context = {'form': rqt_form,
               'request_item': item}
    return render(request, 'request_itemUpdate.html', context)

def singUpView(request):
    message=''
    if request.method=="POST":
        signup= UserCreationForm(request.POST)

        if signup.is_valid():
           
            signup.save()
            messages.success(request, "Product added")
        else:
            message ="An error occurred"
    else:
        signup = UserCreationForm()
    context ={
            'form': signup,
            message: message
        }

    return render(request, 'registration/sign_up.html', context)
