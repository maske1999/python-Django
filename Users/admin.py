from Users.apps import UsersConfig
from Users.models import Post
from django.contrib.auth.models import User

from django.contrib import admin
# Register your models here.
admin.site.register(Post)