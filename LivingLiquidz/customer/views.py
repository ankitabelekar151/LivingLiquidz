from django.shortcuts import render,redirect
from seller.models import Product, Category,Sub_Category,Sub_Sub_Category,StatePrice
from django.http import JsonResponse,HttpRequest,HttpResponseNotFound


# Create your views here.

def search_suggestions(request):
    search = request.GET.get('search')
    payload = []
    if search:
        suggestions = Product.objects.filter(title__icontains=search)
        # for i in suggestions:
        #  print('kkkkkkkkkkkkkkkkkkkkkkkkk',i.id,i.title)
        for s in suggestions:
            payload.append({'id': s.id, 'title': s.title})     
    return JsonResponse({'status': 200,'payload': payload})

    
def category_products(request,id):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.get(id=id)
    products = Product.objects.filter(sub_sub_category__name=sub_sub_category.name)
    
    state_prices = StatePrice.objects.filter(product__in=products)

    
    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        'products': products,
        'state_prices': state_prices,
    }
    return render(request,'customer/category_products.html',context)

def product_details(request,id):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.get(id=id)
    try:
        product = Product.objects.get(id=id)
        sub_sub_category = product.sub_sub_category
        all_products = Product.objects.filter(sub_sub_category=sub_sub_category).exclude(id=id)
        state_price = StatePrice.objects.filter(product=product)
    except StatePrice.DoesNotExist:
        state_price = None 
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")

    context = {
               'category':category,
               'sub_category':sub_category,
               'sub_sub_category':sub_sub_category,
               'product': product,
               'state_price':state_price,
               'all_products':all_products,
               }  


    return render(request, 'customer/product_details.html',context)

def whisky(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/whisky.html',context)

def wine(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/wine.html',context)

def vodka(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/vodka.html',context)

def beer(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/beer.html',context)

def about(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/otherPages/about.html',context)

def contact(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/otherPages/contact.html',context)

def privacyPolicy(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/otherPages/privacyPolicy.html',context)

def termsConditions(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/otherPages/termsConditions.html',context)

def faq(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sub_sub_category = Sub_Sub_Category.objects.all()

    context = {
        'category':category,
        'sub_category':sub_category,
        'sub_sub_category': sub_sub_category,
        
    }
    return render(request,'customer/otherPages/faq.html',context)
