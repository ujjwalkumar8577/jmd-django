"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order, name='order'),
    path('store/', views.store, name='store'),
    path('product/<str:slug>', views.product, name='product'),
    path('party/', views.party, name='party'),
    path('adminportal/', views.adminportal, name='adminportal'),
    path('ordersheet/', views.ordersheet, name='ordersheet'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('ujjwal/', views.ujjwal, name='ujjwal')
]
