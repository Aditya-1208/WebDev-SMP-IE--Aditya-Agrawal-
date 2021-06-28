from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class user_avatar(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,null=True)
    avatar_svg = models.TextField(null=True)