from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)