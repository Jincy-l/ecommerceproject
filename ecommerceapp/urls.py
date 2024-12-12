from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
   
    # path("", views.main_index, name='mainindex'),

    # path("mainindex",views.main_index,name='mainindex'),
    
    path("",views.index,name='index'),
    path("index",views.index,name='index'),
    path("mainindex",views.main_index,name='mainindex'),
    path("blog",views.blog,name='blog'),
    path("blogDetails",views.blogDetails,name='blogDetails'),
    path("checkOut",views.checkOut,name='checkOut'),
    path("contactUs",views.contactUs,name='contactUs'),
    path("shopDetails",views.shopDetails,name='shopDetails'),
    path("shopingCart",views.shopingCart,name='shopingCart'),
    path("login",views.login,name='login')
    
    
]
