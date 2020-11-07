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
    product= sellproduct.objects.all()
    return render(request,'productview.html',{'p':product})
class productsView(ListView):
    def get(self,request):
        allproducts=sellproduct.objects.all()
        return render(request,'buy.html',{'products_list':allproducts})
def sellit(request):
    sellform=sell(request.POST or None)
    return render(request,'sell.html',{'form':sellform})
def soldform(request):
    name=request.POST.get('name',False)
    product=request.POST.get('product',False)
    cost=request.POST.get('cost',False)
    image=request.FILES['image']
    allproducts=sellproduct.objects.create(name=name,product=product,cost=cost,image=image)
    return render(request,'thankyou.html')