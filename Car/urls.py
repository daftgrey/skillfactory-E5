from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('manufacturer/<str:slug>/', GetMan.as_view(), name='manufacturer'),
    path('car/<str:slug>/', GetCar.as_view(), name='car'),
    path('search/', Search.as_view(), name='search'),
    path('about_us', about_us, name='about_us')
]
