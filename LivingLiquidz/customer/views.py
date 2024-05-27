from django.shortcuts import render
from seller.models import Product, Category
from .models import StatePrice
from django.http import JsonResponse


# Create your views here.
def indian_whisky_blended(request):
    

    comparison_results = {} 
    
    if request.method == 'POST' and 'product_id' in request.POST:
        product_id = request.POST['product_id']
        product = Product.objects.get(id=product_id)
        state_prices = StatePrice.objects.filter(product=product)
        comparison_results = {state_price.state: state_price.price for state_price in state_prices}
    
        # Convert JSON data into an HTML table
        table_data = '<table>'
        table_data += '<tr><th>State</th><th>Price</th></tr>'
        for state, price in comparison_results.items():
            table_data += f'<tr><td>{state}</td><td>{price}</td></tr>'
        table_data += '</table>'
        
        return render(request, 'customer/indian_whisky_premium.html', {'table_data': table_data})

    category = Category.objects.get(name="Indian whisky blended")
    indian_whisky_blended = Product.objects.filter(category=category)

    context = {
        'indian_whisky_blended':indian_whisky_blended,
        }
    return render(request, 'customer/indian_whisky_blended.html',context)

def indian_whisky_premium(request):
    comparison_results = {} 
    
    if request.method == 'POST' and 'product_id' in request.POST:
        product_id = request.POST['product_id']
        product = Product.objects.get(id=product_id)
        state_prices = StatePrice.objects.filter(product=product)
        comparison_results = {state_price.state: state_price.price for state_price in state_prices}
    
        # Convert JSON data into an HTML table
        table_data = '<table>'
        table_data += '<tr><th>State</th><th>Price</th></tr>'
        for state, price in comparison_results.items():
            table_data += f'<tr><td>{state}</td><td>{price}</td></tr>'
        table_data += '</table>'
        
        return render(request, 'customer/indian_whisky_premium.html', {'table_data': table_data})
    
    category = Category.objects.get(name="Indian Whisky Premium")
    indian_whisky_premium = Product.objects.filter(category=category)
    context = {
        'indian_whisky_premium':indian_whisky_premium
        }
    return render(request, 'customer/indian_whisky_premium.html',context)

def indian_vodka_flavoured(request):
    category = Category.objects.get(name="Indian Vodka Flavoured")
    indian_vodka_flavoured = Product.objects.filter(category=category)
    context = {
        'indian_vodka_flavoured':indian_vodka_flavoured
    }
    return render(request, 'customer/indian_vodka_flavoured.html',context)

def indian_vodka_flavoured(request):
    category = Category.objects.get(name="Indian Vodka Flavoured")
    indian_vodka_flavoured = Product.objects.filter(category=category)
    context = {
        'indian_vodka_flavoured':indian_vodka_flavoured
    }
    return render(request, 'customer/indian_vodka_flavoured.html',context)

def indian_vodka_plain(request):
    category = Category.objects.get(name="Indian Vodka Plain")
    indian_vodka_plain = Product.objects.filter(category=category)
    context = {
        'indian_vodka_plain':indian_vodka_plain
    }
    return render(request, 'customer/indian_vodka_plain.html',context)

def imported_vodka_flavoured(request):
    category = Category.objects.get(name="Imported Vodka Flavoured")
    imported_vodka_flavoured = Product.objects.filter(category=category)
    context = {
        'imported_vodka_flavoured':imported_vodka_flavoured
    }
    return render(request, 'customer/imported_vodka_flavoured.html',context)

def imported_vodka_plain(request):
    category = Category.objects.get(name="Imported Vodka Plain")
    imported_vodka_plain = Product.objects.filter(category=category)
    context = {
        'imported_vodka_plain':imported_vodka_plain
    }
    return render(request, 'customer/imported_vodka_plain.html',context)

def whisky(request):
    return render(request, 'customer/whisky.html')