from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=4000)
    likes = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.CharField(max_length=4000)
    likes = models.PositiveIntegerField()
    last_updated = models.DateTimeField(default=timezone.now)
    parent_comment_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


