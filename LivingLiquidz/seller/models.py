from django.db import models
from login.models import *
from datetime import datetime

# Create your models here.

# from mptt.models import MPTTModel, TreeForeignKey


# class Category(MPTTModel):
#     STATUS = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
    
#     parent = TreeForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)
#     title = models.CharField(max_length=150)
#     keywords = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     product_image = models.ImageField(upload_to='upload_products',blank=True)
#     status = models.CharField(max_length=10, choices=STATUS)
#     slug = models.SlugField()
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now_add=True)

#     class MPTTMeta:
#         order_insertion_by = ['title']

#     def __str__(self):
#         return self.title

# class Product(models.Model):
#     STATUS = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     user = models.ForeignKey(LlUser, on_delete=models.CASCADE)
#     title = models.CharField(max_length=150)
#     keywords = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     product_image = models.ImageField(upload_to='upload_products',blank=True)
#     selling_price = models.FloatField()
#     quantity= models.IntegerField()
#     size= models.CharField(max_length=100)

#     objects = models.Manager()
    
#     def __str__(self):
#         return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
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
