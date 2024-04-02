from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from login.models import *
from seller.models import *

# Create your views here.
@login_required
def admin_base(request):
    return render(request,'admin_base.html')


def seller_register_list(request):
    sellers = LlUser.objects.filter(is_seller=False,is_admin=False,is_customer=False) 
    data = seller_user.objects.filter(is_seller=False)
    context = {
        'sellers': sellers, 
        'data':data,
    }
    return render(request,'admin/seller_register_list.html',context)

def seller_profile_view(request,id):
    data1=seller_user.objects.get(id=id)
    # print('ssss',id)
    if request.method =='POST':
        commision = request.POST.get('commision')
        print('uuuuuuuuuuuuuu',commision)
        data1.commision = request.POST.get('commision')
        # data.company_adress=request.POST.get('company_adress')
        # data.company_name=request.POST.get('company_name')
        data1.save()
        print("sdfghjkl;",data1.first_name)
        if request.method == 'POST':
            if request.POST.get("is_seller") == "approval_button":
                data1.is_seller = True
                data1.seller_approved= True
                data1.save()
            elif request.POST.get("seller_reject") == "reject_button":
                data1.seller_reject = True
                data1.is_seller = False
                data1.seller_approved= False
                data1.save()

            # Redirect to another page or do something else after saving
        return redirect('/seller_register_list/')
    context = {'data1': data1}
    return render(request, 'admin/seller_profile_view.html', context)

def seller_approved_list(request):
    data1=seller_user.objects.filter(seller_approved=True)
    context={
        "data1":data1,
    }
    return render(request, 'admin/seller_approved_list.html', context)

def seller_reject_list(request):
    data1=seller_user.objects.filter(seller_reject=True)
    context={
        "data1":data1,
    }
    return render(request, 'admin/seller_reject_list.html', context)
