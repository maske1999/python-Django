from django.db import models
from django.contrib.auth.models import User

# Create your models her 
class Post(models.Model):
    username=models.ForeignKey(User, verbose_name="username",default=1, on_delete=models.CASCADE)
    Message=models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)