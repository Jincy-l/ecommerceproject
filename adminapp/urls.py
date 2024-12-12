from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
   
    # path("", views.main_index, name='mainindex'),

    # path("mainindex",views.main_index,name='mainindex'),
    
    path("",views.index,name='index'),
] 