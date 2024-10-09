from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from login.models import *
from seller.models import *

# Create your views here.
@login_required
def admin_base(request):
    return render(request,'admin/admin_base.html')

@login_required
def add_products(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        brand = request.POST.get('brand')
        product_image = request.FILES.get('product_image')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        sub_sub_category_id = request.POST.get('sub_sub_category')
        user_id = request.POST.get('user')
        
        sub_sub_category = Sub_Sub_Category.objects.get(id=sub_sub_category_id)
        user = LlUser.objects.get(id=user_id)
        
        product = Product.objects.create(
            sub_sub_category=sub_sub_category,
            user=user,
            title=title,
            description=description,
            brand=brand,
            product_image=product_image,
            price=price,
            quantity=quantity,
            size=size,
            product_date=datetime.now()
        )
        
        return redirect('/add_products/') 

    sub_sub_categories = Sub_Sub_Category.objects.all()
    users = LlUser.objects.all()
    states = StatePrice.STATES
    
    
    context = {
        'sub_sub_categories': sub_sub_categories,
        'users': users,
        'states': states,
    }
    return render(request,'admin/add_products.html',context)

@login_required
def add_state_prices(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        state = request.POST.get('state')
        size_90ml = request.POST.get('size_90ml')
        size_180ml = request.POST.get('size_180ml')
        size_375ml = request.POST.get('size_375ml')
        size_750ml = request.POST.get('size_750ml')
        size_1ltr = request.POST.get('size_1ltr')
        size_2000ml = request.POST.get('size_2000ml')

        product = Product.objects.get(id=product_id)

        StatePrice.objects.create(
            product=product,
            state=state,
            size_90ml=size_90ml,
            size_180ml=size_180ml,
            size_375ml=size_375ml,
            size_750ml=size_750ml,
            size_1ltr=size_1ltr,
            size_2000ml=size_2000ml
        )

        return redirect('/add_state_prices/') 
    
    products= Product.objects.all()
    states = StatePrice.STATES

    context={
        'products':products,
        'states':states,
    }
    return render(request,'admin/add_state_prices.html', context)

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
