from django.urls import path, include,re_path
from .views import home
from . import views


urlpatterns = [
    path("", home, name="home"),
    path("customer_signup/", views.customer_signup, name="customer_signup"),
    path("customer_signin/", views.customer_signin, name="customer_signin"),
    path("customer_logout/", views.customer_logout, name="customer_logout"),
    path("seller_signup/", views.seller_signup, name="seller_signup"),
    path("seller_signin/", views.seller_signin, name="seller_signin"),
    path("seller_logout/", views.seller_logout, name="seller_logout"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),
]