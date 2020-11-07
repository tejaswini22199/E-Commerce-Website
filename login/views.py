from django.shortcuts import render
from .forms import sell
# Create your views here.
def home(request):
    return render(request,'home.html')
def dashboard(request):
    return render(request,'login.html')
def buy(request):
    return render(request,'buy.html')
def sellit(request):
    sellform=sell(request.POST or None)
    return render(request,'sell.html',{'form':sellform})