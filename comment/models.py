from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from blog.models import Post


class Comments(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.body


