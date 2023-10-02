from django.urls import path
from. import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:id>/', views.post, name='post'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('post', views.form, name='form'),
]