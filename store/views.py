from django.shortcuts import render,redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductForm
from django.http import HttpResponseRedirect

# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer , complete = False)
        
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        

    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0 , 'shippping':False}
        cart_items = order['get_cart_items']


    products = Product.objects.all()
    context = {'products':products ,'cart_items': cart_items}
    return render(request,'index.html' , context)


@login_required(login_url='/accounts/login/')  
def new_post(request):
    current_user = request.user
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect(store)
    else:
        form = ProductForm()
    return render(request, 'newpost.html',{"form":form})
