import django
from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.urls.conf import include
from . import views
app_name = 'users'
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('mylogin',views.mylogin,name="mylogin"),
    path('register',views.register,name='register'),
    path('logout',views.my_logout,name='my_logout'),
    path('profile/<int:profile_id>',views.profile,name='profile')
]