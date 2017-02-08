from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextField()
    image = models.ImageField(upload_to="blog_image", blank=True, null=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_comment(self):
        from comment.models import Comments
        comments = Comments.objects.filter(article=self.id, publish=True)
        return comments

    def get_absolute_url(self):
        return reverse('post:post', args=[self.id])


# Create your models here.
