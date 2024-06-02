from django.shortcuts import render,redirect
from seller.models import Product, Category,Sub_Category,Sub_Sub_Category,StatePrice
from django.http import JsonResponse,HttpRequest,HttpResponseNotFound


# Create your views here.

def search_suggestions(request):
    search = request.GET.get('search')
    payload = []
    if search:
        suggestions = Product.objects.filter(title__startswith=search)
        for s in suggestions:
            payload.append(s.title)     
    return JsonResponse({'status': 200,'title': payload})

    
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
  
    # try:
    #     product = Product.objects.get(id=id)
    #     size_price = SizePrice.objects.get(product=product)
    # except SizePrice.DoesNotExist:
    #     size_price = None 
    # except Product.DoesNotExist:
    #     return HttpResponseNotFound("Product not found")

    # context = {'product': product,
    #            'size_price':size_price}  

    return render(request, 'customer/product_details.html')

    
# def indian_whisky_blended(request):
#     comparison_results = {} 
#     if request.method == 'POST' and 'product_id' in request.POST:
#         product_id = request.POST['product_id']
#         product = Product.objects.get(id=product_id)
#         # state_prices = StatePrice.objects.filter(product=product)
#         # comparison_results = {state_price.state: state_price.price for state_price in state_prices}
    
#         # Convert JSON data into an HTML table
#         table_data = '<table>'
#         table_data += '<tr><th>State</th><th>Price</th></tr>'
#         for state, price in comparison_results.items():
#             table_data += f'<tr><td>{state}</td><td>{price}</td></tr>'
#         table_data += '</table>'
        
#         return render(request, 'customer/indian_whisky_premium.html', {'table_data': table_data})

#     category = Category.objects.get(name="Indian whisky blended")
#     indian_whisky_blended = Product.objects.filter(category=category)

#     context = {
#         'indian_whisky_blended':indian_whisky_blended,
#         }
#     return render(request, 'customer/indian_whisky_blended.html',context)

# def indian_whisky_premium(request):
#     comparison_results = {} 
    
#     if request.method == 'POST' and 'product_id' in request.POST:
#         product_id = request.POST['product_id']
#         product = Product.objects.get(id=product_id)
#         state_prices = StatePrice.objects.filter(product=product)
#         comparison_results = {state_price.state: state_price.price for state_price in state_prices}
    
#         # Convert JSON data into an HTML table
#         table_data = '<table>'
#         table_data += '<tr><th>State</th><th>Price</th></tr>'
#         for state, price in comparison_results.items():
#             table_data += f'<tr><td>{state}</td><td>{price}</td></tr>'
#         table_data += '</table>'
        
#         return render(request, 'customer/indian_whisky_premium.html', {'table_data': table_data})
    
#     category = Category.objects.get(name="Indian Whisky Premium")
#     indian_whisky_premium = Product.objects.filter(category=category)
#     context = {
#         'indian_whisky_premium':indian_whisky_premium
#         }
#     return render(request, 'customer/indian_whisky_premium.html',context)

