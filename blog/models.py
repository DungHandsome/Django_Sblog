from django.db import models
from django.contrib.auth.models import User
from django.forms import forms

# Create your models here.

class ListTruyen(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    

    
class BlogPost(models.Model):
    botruyen = models.ForeignKey(ListTruyen, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title