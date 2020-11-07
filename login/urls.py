from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.dashboard,name='login'),
    path('login/buy',views.productsView.as_view(),name='buy'),
    path('login/sell',views.sellit,name='sellit'),
    path('login/sold',views.soldform,name='soldform'),
    path('login/buy/<int:pk>',views.productview,name='productdetail')
]