from django.shortcuts import render
from .models import BlogPost
# Create your views here.
def blog(request):
    Data = {'Posts': BlogPost.objects.all().order_by('-time')}
    return render(request, 'blog/blog.html', Data)
def post(request, id):
    post = BlogPost.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})