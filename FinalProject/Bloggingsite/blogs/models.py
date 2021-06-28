from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_n_time = DateTimeField(auto_now_add=True,null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    owner = models.ForeignKey(User,on_delete=CASCADE)
    def __t__(self):
        return self.title
