from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def seller_base(request):
    return render(request, "seller_base.html")