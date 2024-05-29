from django.db import models
from seller.models import Product

# Create your models here.

# class StatePrice(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     state = models.CharField(max_length=100)
#     price = models.FloatField()

#     def __str__(self):
#         return f"{self.product} - {self.state}"
    

# class Size(models.Model):
#     product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
#     size = models.CharField(max_length=100)
#     price = models.FloatField()

#     def __str__(self):
#         return f"{self.product} - {self.size}ml - {self.price}"
