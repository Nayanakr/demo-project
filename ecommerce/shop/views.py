from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from shop.models import Category

from shop.models import Product

from django.contrib.auth.models import User


# Create your views here.

def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

@login_required
def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request, 'product.html', {'c': c,'p':p})
@login_required
def details(request,p):
    d=Product.objects.get(name=p)
    return render(request,'detail.html',{'d':d})

def register(request):
    if (request.method == "POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        fname=request.POST['f']
        lname=request.POST['l']
        em=request.POST['e']


        if (p==cp):
            user=User.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=em)
            user.save()
            return redirect('shop:allcat')
        else:
            return HttpResponse("Passwords are not same")

    return render(request,'register.html')

def userlogin(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)    #buit in function
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("invalid credential")

    return render(request,'login.html')

@login_required
def userlogout(request):
    logout(request)
    return redirect('shop:userlogin')
