from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from .models import Product,Category
from .froms import SignUpForm



def home(request):
    products=Product.objects.all()
    return render(request, 'home.html',{'products':products })
def category(request,foo):
    foo=foo.replace('-',' ')
    #grap the category from the url
    try:
        # look up the category
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})

    except:
        messages.success(request,('that category does not exist'))
        return redirect('home')

    

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def about(request):
    return render(request, 'about.html',{})

def login_user(request):
    if request.method == 'POST':
        username=request.POST('username')
        password=request.POST('password')
        user=authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('you have been logged in'))
            return redirect('home')
        else:
            messages.success(request,('There was an error, please try again'))
            return redirect('login')
        
    else:
        return render(request, 'login.html',{})
def logout_user(request):
    logout(request)
    messages.success(request,("you have logged out successfully ")) 
    return redirect('home')

def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            # log in user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('you have registerd succesfuly'))
            return redirect('home')
        else:
            messages.success(request,('please try again'))
            return redirect('register')
    else:
        return render(request, 'register.html',{'form':form})