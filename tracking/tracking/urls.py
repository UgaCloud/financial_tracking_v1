"""
URL configuration for tracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from noah.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='home_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup_view/', singUpView, name='sign_up'),

    path('departments/', department_list, name='department_list'),
    path('create_dpt/', create_department_view, name ='department_added' ),
    path('update_dpt/<int:dpt_id>/', department_update, name='update_department'),
    path('payments/', payment_create, name = 'add_payment'),
    path('update_pay/<int:pay_id>/', payment_update, name ='payment_update'),
    path('banking/', banking_create, name = 'add_banking'),
    path('update_banking/<int:bank_id>/', banking_update, name = 'edit_banking'),
    path('expense', expense_create, name = 'add_expenses'),
    path('update_expense/<int:exp_id>/',expense_update, name = 'edit_expenses'),
    path('exp_break/', expBreak_create, name = 'add_break'),
    path('update_break/<int:bk_id>/', expbreak_update, name = 'edit_break'),
    path('request', create_request_view, name = 'add_request'),
    path('update_request/<int:rqst_id>/', request_update, name = 'edit_request'),
    path('item_request', create_request_item_view, name = 'add_item'),
    path('item_update/<int:it_id>/', item_request_update, name = 'update_item'),
    path('delete_department/<int:dpt_id>/', delete_department_view, name='delete_dpt'),
    path('delete_payment/<int:pay_id>/', delete_payment_view, name='delete_pay'),
    path('delete_bank/<int:bank_id>/', delete_bank_view, name='delete_banking'),
    path('delete_expense/<int:exp_id>/', delete_expense_view, name='delete_expenses'),
    path('delete_exp_break/<int:bk_id>/', delete_exp_break_view, name='deleteBreak'),
    path('delete_request/<int:rqst_id>/', delete_request_view, name='deleteRequest'),
    path('delete_request_item/<int:it_id>/', delete_request_item_view, name='deleteRequestItem'),








]
