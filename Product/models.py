from django.db import models

# Create your models here.
class ProductDBRouter(models.Model):
    productname=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)