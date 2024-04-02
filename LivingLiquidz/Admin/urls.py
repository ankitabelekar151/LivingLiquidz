from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path("admin_base/", views.admin_base, name="admin_base"),
    path('seller_register_list/',views.seller_register_list,name="seller_register_list"),
    path('seller_profile_view/<int:id>/',views.seller_profile_view,name="seller_profile_view"),
    path('seller_approved_list/',views.seller_approved_list,name="seller_approved_list"),
    path('seller_reject_list/',views.seller_reject_list,name="seller_reject_list"),
]