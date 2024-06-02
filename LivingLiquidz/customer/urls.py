from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path('category_products/<id>',views.category_products,name="category_products"),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
    path('product_details/<id>', views.product_details, name='product_details'),
]