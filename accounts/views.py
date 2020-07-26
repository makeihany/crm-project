from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

def home(request):
    customers = Customers.objects.all()
    orders = Order.objects.all()
    ordercounts = orders.count()
    pendingorder = orders.filter(status='Pending').count()
    deliveredorder = orders.filter(status='Delivered').count()
    context = {'customers':customers, 'orders':orders,'ordercounts':ordercounts,'deliveredorder':deliveredorder,'pendingorder':pendingorder}
    return render(request,'accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/Products.html',{'products':products})

def customers(request,pk_id):
    customer = Customers.objects.get(id=pk_id)
    customer_orders = customer.order_set.all()
    customer_ordersCount = customer_orders.count()
    context = {'customer':customer,'customer_orders':customer_orders, 'customer_ordersCount':customer_ordersCount}
    return render(request, 'accounts/customers.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk_id):
    order = Order.objects.get(id=pk_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
