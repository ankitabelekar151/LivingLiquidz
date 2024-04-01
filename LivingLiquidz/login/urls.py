from django.urls import path, include,re_path
from .views import home
from . import views


urlpatterns = [
    path("", home, name="home"),
    path("customer_signup/", views.customer_signup, name="customer_signup"),
]