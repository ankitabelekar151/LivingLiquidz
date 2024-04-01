from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home_page.html')

def customer_signup(request):
    return render(request, 'login/customer_signup.html')