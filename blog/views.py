from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def blog(request):
    Data = {'Posts': BlogPost.objects.all().order_by('-time')}
    return render(request, 'blog/blog.html', Data)

@login_required
def post(request, id):
    post = BlogPost.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})

@login_required
def form(request):
    if request.method == 'POST':
        if request.POST.get('author') and request.POST.get('title') and request.POST.get('content'):
            post=BlogPost()
            post.author = request.POST.get('author')
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()
            return render(request, 'blog/form.html')  
    else:
        return render(request,'blog/form.html')



def signup_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("blog")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="user/signup.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("blog")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="user/login.html", context={"login_form":form})


@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("blog")