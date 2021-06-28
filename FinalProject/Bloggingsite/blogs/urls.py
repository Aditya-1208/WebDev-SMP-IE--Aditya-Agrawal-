from django.urls import path
from . import views

app_name ='blogs'
urlpatterns=[
    path('',views.home,name="home"),
    path('about',views.about,name='about'),
    path('myblogs',views.myblogs,name="myblogs"),
    path('post/<int:blog_id>',views.post,name="post"),
    path('new_post',views.new_post,name="new_post"),
    path('edit_post/<int:post_id>',views.edit_post,name="edit_post"),
    path('delete_post/<int:post_id>',views.delete_post,name="delete_post")
]