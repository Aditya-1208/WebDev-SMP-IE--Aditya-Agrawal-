from blogs.models import BlogPost
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import user_avatar
# Create your views here.
def mylogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully logged in!")
            return redirect(request.path)
        else:
            messages.error(request,"Invalid Credentials, please try again!")
            return redirect('blogs:home')
    else:
        return redirect('blogs:home')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        avatar_data = request.POST.get('avatar_data')
        #check if pass1 == pass2 and other things
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('users:register')
        if pass1!=pass2:
            messages.error(request, "Both Passwords didn't match,please try again")
            return redirect('users:register')
        
        user = User.objects.create_user(username,email,pass1)
        avatar = user_avatar.objects.create(user = user)
        avatar.avatar_svg = avatar_data
        user.first_name = fname
        user.last_name = lname
        user.save()
        avatar.save()
        messages.success(request,"You have Registered Successfully!")
        return redirect('blogs:home')
    return render(request,'registration/register.html')
def my_logout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out!")
    return redirect('blogs:home')
def profile(request,profile_id):
    profiled_user = User.objects.get(id = profile_id)
    blogs_by_user = BlogPost.objects.filter(owner=profiled_user)
    print(blogs_by_user)
    context = {
        'user_concerned':User.objects.get(id = profile_id).username,
        'full_name':User.objects.get(id = profile_id).first_name +" " + User.objects.get(id = profile_id).last_name,
        'blogs_by_user': blogs_by_user
    }
    return render(request,'users/userprofile.html', context)