from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.TextField(null=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(BlogPost)