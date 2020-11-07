from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.dashboard,name='login'),
    path('login/buy',views.buy,name='buy'),
    path('login/sell',views.sellit,name='sellit')

]
