from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404, render
from .forms import sell
from .models import sellproduct
from django.views.generic import ListView  ,DetailView, UpdateView ,DeleteView
# Create your views here.
def home(request):
    return render(request,'home.html')
def dashboard(request):
    return render(request,'login.html')
def buy(request):
    return render(request,'buy.html')
def productview(request,pk):
    product= get_object_or_404(sellproduct,pk=pk)
    return render(request,'productview.html',{'x':product})
class productsView(ListView):
    def get(self,request):
        allproducts=sellproduct.objects.all().filter(issold=False)
        return render(request,'buy.html',{'products_list':allproducts})
def sellit(request):
    sellform=sell(request.POST or None)
    return render(request,'sell.html',{'form':sellform})
def soldform(request):
    name=request.POST.get('name',False)
    product=request.POST.get('product',False)
    cost=request.POST.get('cost',False)
    image=request.FILES.get('image')
    phonenumber=request.POST.get('phonenumber')
    sellproduct.objects.create(name=name,product=product,cost=cost,image=image,phonenumber=phonenumber)
    return render(request,'thankyou.html')
def conformorder(request,pk):
    pro=get_object_or_404(sellproduct,pk=pk)
    pro.issold=True
    pro.save()
    return render(request,'final.html')
