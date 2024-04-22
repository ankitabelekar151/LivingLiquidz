from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def seller_base(request):
    return render(request, "seller/seller_dashboard.html")

@login_required
def seller_add_product(request):
    return render(request, 'seller/seller_add_product.html')