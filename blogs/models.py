from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images')
    tags = models.ManyToManyField(Tags)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title   

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    