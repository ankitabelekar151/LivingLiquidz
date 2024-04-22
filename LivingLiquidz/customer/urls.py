from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path('indian_whisky_blended/',views.indian_whisky_blended,name="indian_whisky_blended"),
    path('indian_whisky_premium/',views.indian_whisky_premium,name="indian_whisky_premium"),
    path('indian_vodka_flavoured/',views.indian_vodka_flavoured,name="indian_vodka_flavoured"),
    path('indian_vodka_plain/',views.indian_vodka_plain,name="indian_vodka_plain"),
    path('imported_vodka_flavoured/',views.imported_vodka_flavoured,name="imported_vodka_flavoured"),
    
]