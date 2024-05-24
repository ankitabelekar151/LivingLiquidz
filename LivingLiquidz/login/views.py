# Create your views here.
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import LlUser, customer_user, seller_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from seller.models import Category,Sub_Category,Sub_Sub_Category


def home(request):
    cat = Category.objects.all()
    sub = Sub_Category.objects.all()
    s = Sub_Sub_Category.objects.all()
    # for i in s:
    #     if i.sub_category.name == 'Indian-Whisky':
    #         print('llllllllllllllllllllllllll',i.sub_category)
    #     else:
    #         print('jjjjjjjjjjjjjjjjjjjjj')
    context = {'cat':cat}
    return render(request, 'base.html',context)

def generate_otp():
    return ''.join(random.choices('0123456789', k=6))

def customer_signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        mydata = LlUser(first_name=first_name, last_name=last_name, email=email, username=email, mobile_number=mobile_number,is_Lluser=True,is_customer=True,is_active=True)
        mydata.set_password(password)
        mydata.save()
        
        customer_profile = customer_user(user=mydata, first_name=first_name, last_name=last_name, email=email, mobile_number=mobile_number, is_customer=True,is_active=True)
        customer_profile.save()

        subject = "Customer Registration Confirmation"
        message = f"Hello {mydata.first_name} {mydata.last_name},\n\nThank you for registering as a customer on our website. Your account has been successfully created.\n\n"
        message += f"Your login details:\n"
        message += f"Username: {mydata.email}\n"
        message += f"Password: {password}\n\n"  # Replace [YourGeneratedPassword] with the actual generated password
        login_url = "http://livingliquidz.com/customer_signin/"  # Replace 'seller_login' with the actual name of your seller login URL pattern
        message += f"To log in, please visit: {login_url}\n\n"
        message += "Best regards,\nLiquor Legends Team"
        from_email = "ankitabelekar151@gmail.com.com"  # Replace this with your desired 'from' email address
        recipient_list = [mydata.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect('/customer_signin/')
    return render(request, 'login/customer_signup.html')


def customer_signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        LlUser = authenticate(email=email, password=password)
        print("userr",LlUser)

        if LlUser is not None and LlUser.is_customer:
            # Log in the user
            login(request,LlUser)
            
            return redirect('/')  
        else:
           
            error_message = "Invalid login credentials. Please try again."
            messages.error(request, error_message)
            # return render(request, 'registeration/customer_register.html', {'error_message': error_message})

    return render(request, 'login/customer_signin.html')

def customer_logout(request):
    logout(request)
    return redirect('/')

def seller_signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        mydata = LlUser(first_name=first_name, last_name=last_name, email=email,username=email, mobile_number=mobile_number,is_Lluser=True,is_active=True,is_seller=True)
        mydata.set_password(password)
        mydata.save()
        
        seller_profile = seller_user(user=mydata, first_name=first_name, last_name=last_name, email=email, mobile_number=mobile_number, is_seller=False,is_active=True)
        seller_profile.save()
        
        subject = "Seller Registration Confirmation"
        message = f"Hello {mydata.first_name} {mydata.last_name},\n\nThank you for registering as a seller on our website. Your account has been successfully created.\n\n"
        message += f"Your login details:\n"
        message += f"Username: {mydata.email}\n"
        message += f"Password: {password}\n\n"  # Replace [YourGeneratedPassword] with the actual generated password
        login_url = "http://livingliquidz/seller_signin/"  # Replace 'seller_login' with the actual name of your seller login URL pattern
        message += f"To log in, please visit: {login_url}\n\n"
        message += "Best regards,\nLL Team"
        from_email = "ankitabelekar151@gmail.com" 
        recipient_list = [mydata.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        return redirect('/seller_signin/')
    return render(request, 'login/seller_signup.html')

def seller_signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        ll_user = authenticate(email=email, password=password)

        if ll_user is not None:
            # Get the associated seller_user instance
            try:
                seller_profile = seller_user.objects.get(user=ll_user)
            except seller_user.DoesNotExist:
                seller_profile = None

            if seller_profile is not None and seller_profile.is_seller:
                # Log in the user
                login(request, ll_user)
                return redirect('/seller_base/')
            else:
                # Handle the case where the seller_user instance doesn't exist
                error_message = "Seller profile is not approved yet. Please wait for approval."
                messages.error(request, error_message)
        else:
            error_message = "Invalid login credentials. Please try again."
            messages.error(request, error_message)

    return render(request, 'login/seller_signin.html')

def seller_logout(request):
    
    logout(request)
    return redirect('/')
    

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        LlUser = authenticate(email=email, password=password)
        print("userr",LlUser)

        if LlUser is not None and LlUser.is_superuser:
            # Log in the user
            login(request,LlUser)
            
            return redirect('/admin_base/')  
        else:
           
            error_message = "Invalid login credentials. Please try again."
            messages.error(request, error_message)
            # return render(request, 'registeration/customer_register.html', {'error_message': error_message})

    return render(request, 'login/admin_login.html')

def admin_logout(request):
    
    logout(request)
    return redirect('/')
