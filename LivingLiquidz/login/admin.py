from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LlUser,customer_user,seller_user

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'mobile_number', 'is_Lluser', 'is_admin', 'is_staff', 'is_customer', 'is_active','is_seller')
    search_fields = ('email', 'first_name', 'last_name', 'mobile_number')
    list_filter = ('is_Lluser', 'is_admin', 'is_staff', 'is_customer', 'is_active')

admin.site.register(LlUser)
admin.site.register(customer_user)
admin.site.register(seller_user)

