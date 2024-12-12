from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def main_index(request):
    return render(request, 'user_layout/main_index.html')
def blogDetails(request):
    return render(request, 'blog_details.html')
def blog(request):
    return render(request,'blog.html')
def checkOut(request):
    return render(request,'checkout.html')
def contactUs(request):
    return render(request,'contact.html')
def shopDetails(request):
    return render(request,'shop_details.html')
def shopingCart(request):
    return render(request,'shoping_cart.html')
def login(request):
    return render(request,'login.html')
    