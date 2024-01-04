from django.shortcuts import render


# tourism_app/views.py
from django.shortcuts import render, redirect
from .models import Department, Payment, Banking, Expenses, Exp_break, Request, Request_items
from .forms import DepartmentForm, PaymentForm, BankingForm, ExpensesForm, ExpBreakForm, RequestForm, RequestItemsForm

# Add CRUD views for each model (Department, Payment, Banking, Expenses, Exp_break, Request, Request_items).
# Use the patterns from the previous example.

# Example:

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
    return render(request, template_name='department.html', context=context)




def department_update(request, pk):
    department = Department.objects.get(id=pk)
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
    return render(request, 'payment_create.html', context)



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
  form = BankingForm()
  if request.method == 'POST':
    form = BankingForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('banking-details')

  context = {'form': form}
  return render(request, 'banking_create.html', context)


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
  form = ExpensesForm()
  if request.method == 'POST':
    form = ExpensesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('banking-details')

  context = {'form': form}
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
  form = ExpBreakForm()
  if request.method == 'POST':
    form = ExpBreakForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('payment-list')

  context = {'form': form}
  return render(request, 'expbreak_create.html', context)


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
    return render(request, template_name='department.html', context=context)


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
    return render(request, 'department_update.html', context) 