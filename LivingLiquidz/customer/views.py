from django.shortcuts import render
from seller.models import Product, Category

# Create your views here.
def indian_whisky_blended(request):
    category = Category.objects.get(name="Indian whisky blended")
    indian_whisky_blended = Product.objects.filter(category=category)
    context = {
        'indian_whisky_blended':indian_whisky_blended
        }
    return render(request, 'customer/indian_whisky_blended.html',context)

def indian_whisky_premium(request):
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