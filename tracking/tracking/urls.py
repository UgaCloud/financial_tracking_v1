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
    path('update_pay/<int:pk>/', payment_update, name ='payment_update'),
    path('banking/', banking_create, name = 'add_banking'),
    path('update_banking/<int:pk>/', banking_update, name = 'edit_banking'),
    path('expense', expense_create, name = 'add_expenses'),
    path('update_expense/<int:pk>/',expense_update, name = 'edit_expenses'),
    path('exp_break/', expBreak_create, name = 'add_break'),
    path('update_break/<int:pk>/', expbreak_update, name = 'edit_break'),
    path('request', create_request_item_view, name = 'add_request'),
    path('update_request/<int:pk>/', request_update, name = 'edit_reuests'),
    path('item_request', create_request_item_view, name = 'add_item'),
    path('item_update/<int:pk>/', item_request_update, name = 'update_item')

]
