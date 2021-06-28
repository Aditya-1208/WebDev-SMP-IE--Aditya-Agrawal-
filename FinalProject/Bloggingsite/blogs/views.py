from django.contrib import messages
from django.forms.forms import Form
from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import new_post_form,edit_post_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import http
# Create your views here.
def home(request):
    all_blogs = BlogPost.objects.all().order_by('-date_n_time')
    context = {
        'all_blogs':all_blogs
    }
    return render(request,'blogs/home.html',context)
def about(request):
    return render(request,'blogs/about.html')
# @login_required(login_url='users:login')
def myblogs(request):
    if request.user.is_authenticated    :
        blog_entries = BlogPost.objects.filter(owner = request.user)
        context = {
            'blog_entries':blog_entries
        }
        return render(request,'blogs/myblogs.html',context)
    else:
        messages.error(request,"Please login to continue!")
        return redirect('users:login')
def post(request,blog_id):
    blog_entry = BlogPost.objects.get(id=blog_id)
    context = {
        'blog_entry':blog_entry,'request':request,
    }
    return render(request,'blogs/post.html',context)
# @login_required(login_url='users:login')
def new_post(request):
    if request.user.is_authenticated:
        if request.method!='POST':
            form = new_post_form()
        else:
            form = new_post_form(data=request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                post.owner = request.user
                post.save()
                return redirect('blogs:myblogs')
        #if form was not valid then invalid form or empty form will be available if we reach here!
        context = {
            'form':form
        }
        return render(request,'blogs/new_post.html',context)
    else:
        messages.error(request,"Please login to continue!")
        return redirect('users:login')
# @login_required(login_url='users:login')
def edit_post(request,post_id):
    if request.user.is_authenticated:
        if request.user!=BlogPost.objects.get(id=post_id).owner:
            messages.error(request,"You can not edit other's Blogs!")
            return redirect('blogs:post',blog_id=post_id )
        else:
            if request.method!='POST':
                form = edit_post_form(instance=BlogPost.objects.get(id=post_id))
            else:
                form = edit_post_form(data=request.POST,instance=BlogPost.objects.get(id=post_id))
                if form.is_valid():
                    form.save()
                    return redirect('blogs:post',blog_id=post_id)
            context = {
                'form':form,'id':post_id
            }
            return render(request,'blogs/edit_post.html',context)
    else:
        messages.error(request,"Please login to continue!")
        return redirect('users:login')
# @login_required(login_url='users:login')
def delete_post(request,post_id):
    if request.user.is_authenticated:
        if request.user!=BlogPost.objects.get(id=post_id).owner:
            messages.error(request,"You can not delete other's Blogs!")
            return redirect('blogs:post',blog_id=post_id )
        else:
            BlogPost.objects.get(id=post_id).delete()
            return redirect('blogs:myblogs')
    else:
        messages.error(request,"Please login to continue!")
        return redirect('users:login')
