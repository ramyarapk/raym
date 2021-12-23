from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def css(request):
    return render(request,'css.html')

def one(request):
    return render(request,'one_page.html')

def onee(request):
    return render(request,"onepage.html")

def reg(request):
    return render(request,"register.html")