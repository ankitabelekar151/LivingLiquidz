from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path('category_products/<id>',views.category_products,name="category_products"),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('whisky/', views.whisky, name='whisky'),
    path('wine/', views.wine, name='wine'),
    path('vodka/', views.vodka, name='vodka'),
    path('beer/', views.beer, name='beer'),
]