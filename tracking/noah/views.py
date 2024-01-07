from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Department, Payment, Banking, Expenses, Exp_break, Request, Request_items
from .forms import DepartmentForm, PaymentForm, BankingForm, ExpensesForm, ExpBreakForm, RequestForm, RequestItemsForm
@login_required
def IndexView(request):
    return render(request, 'index.html')


@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

@login_required
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
    return render(request, template_name='department_list.html', context=context)



@login_required
def department_update(request, dpt_id):
    department = Department.objects.get(id=dpt_id)
    form = DepartmentForm(instance=department)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
           form.save()
        return redirect(create_department_view)
    else:
       form = DepartmentForm(instance=department)
        
    context = {'form': form}
    return render(request, 'update/edit_department.html', context) 

@login_required
def payment_create(request):
 
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect(payment_create)
    else:
       payment_form = PaymentForm()
    pay = Payment.objects.all()
    context = {'form': payment_form,
               'payment':pay}
    return render(request, 'payment.html', context)


@login_required
def payment_update(request, pay_id):
  payment = Payment.objects.get(id=pay_id)
  form = PaymentForm(instance=payment)

  if request.method == 'POST':
     form = PaymentForm(request.POST, instance=payment)
     if form.is_valid():
       form.save()
       return redirect('payment-list')

  context = {'form': form}
  return render(request, 'update/edit_payment.html', context)

@login_required
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
     'banks': bank
    }
  return render(request, template_name ='banking.html', context = context)

@login_required
def banking_update(request, bank_id):
  banking = Banking.objects.get(id=bank_id)
  form = BankingForm(instance=banking)

  if request.method == 'POST':
     form = BankingForm(request.POST, instance=banking)
     if form.is_valid():
       form.save()
       return redirect(banking_update)

  context = {'form': form}
  return render(request, 'update/edit_banking.html', context)


@login_required
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


@login_required
def expense_update(request, exp_id):
    expense = Expenses.objects.get(id=exp_id)
    form = ExpensesForm(instance=expense)
    
    if request.method == 'POST':
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect(expense_create)
    else:
        form =ExpensesForm(instance = expense)

    context = {'form': form}
    return render(request, 'update/edit_expense.html', context)

@login_required
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

@login_required
def expbreak_update(request, bk_id):
    expbreak = Exp_break.objects.get(id=bk_id)
    form =ExpBreakForm(instance=expbreak)

    if request.method == 'POST':
        brk_form = ExpBreakForm(request.POST, instance=expbreak)
        if brk_form.is_valid():
            brk_form.save()
        return redirect(expBreak_create)
    else:
     brk_form =ExpBreakForm(instance=expbreak)
    context = {'form': form,
               'expbreak': expbreak}
    return render(request, 'update/edit_expbreak.html', context)


@login_required
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

@login_required
def request_update(request, rqst_id):
    requests = Request.objects.get(id=rqst_id)
    rqt_form = RequestForm(instance=requests)

    if request.method == 'POST':
        rqt_form = RequestForm(request.POST, instance=requests)
        if rqt_form.is_valid():
           rqt_form.save()
        return redirect(create_request_view)
    else:
       rqt_form = RequestForm(instance=requests)
        
    context = {'form': rqt_form,
               'request': requests}
    return render(request, 'update/edit_request.html', context) 

@login_required
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
    return render(request, template_name='request_item.html', context=context)

@login_required
def item_request_update(request, it_id):
    item = Request_items.objects.get(id=it_id)
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
    return render(request, 'update/edit_req_item.html', context)


@login_required
def delete_department_view(request, dpt_id):
    dpart =Department.objects.get(id=dpt_id)

    dpart.delete() 
    messages.success(request, "Done")
    return redirect(create_department_view)


@login_required
def delete_payment_view(request, pay_id):
    payment =Payment.objects.get(id=pay_id)

    payment.delete() 
    messages.success(request, "Done")
    return redirect(payment_create)


@login_required
def delete_bank_view(request, bank_id):
    bank =Banking.objects.get(id=bank_id)

    bank.delete() 
    messages.success(request, "Done")
    return redirect(banking_create)


@login_required
def delete_expense_view(request, exp_id):
    expense =Expenses.objects.get(id=exp_id)

    expense.delete() 
    messages.success(request, "Done")
    return redirect(expense_create)



@login_required
def delete_exp_break_view(request, bk_id):
    exp_break =Exp_break.objects.get(id=bk_id)

    exp_break.delete() 
    messages.success(request, "Done")
    return redirect(expBreak_create)


@login_required
def delete_request_view(request, rqst_id):
    req =Request.objects.get(id=rqst_id)

    req.delete() 
    messages.success(request, "Done")
    return redirect(create_request_view)


@login_required
def delete_request_item_view(request, it_id):
    req_item= Request_items.objects.get(id=it_id)

    req_item.delete() 
    messages.success(request, "Done")
    return redirect(create_request_view)


@login_required
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
