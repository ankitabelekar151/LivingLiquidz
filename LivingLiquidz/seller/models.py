from django.db import models
from login.models import *
from datetime import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Sub_Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.sub_category} - {self.name}"

    
class Product(models.Model):
    sub_sub_category = models.ForeignKey(Sub_Sub_Category, on_delete=models.CASCADE)
    user = models.ForeignKey(LlUser, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=150,blank=True, null=True)
    description = models.CharField(max_length=255,blank=True, null=True)
    brand = models.CharField(max_length=100,blank=True, null=True)
    product_image = models.ImageField(upload_to='upload_products',blank=True,null=True,default="")
    price = models.FloatField(null=True, blank=True)
    product_date=models.DateTimeField(default=datetime.now, blank=True)
    # product_approved = models.BooleanField(default=False)
    # product_reject = models.BooleanField(default=False)
    quantity= models.CharField(max_length=100,default="",null=True,blank=True)
    size= models.CharField(max_length=100,default="",null=True,blank=True)
    product_id=models.CharField(max_length=100,default="",null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

