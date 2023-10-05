from django.db import models
from django.contrib.auth.models import User
from django.forms import forms
# Create your models here.
class BlogPost(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)