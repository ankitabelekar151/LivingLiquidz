from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path('seller_base/',views.seller_base,name="seller_base"),
    path('seller_add_product/', views.seller_add_product, name='seller_add_product'),
]