from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from account.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    title = models.CharField(_('title'),max_length=50,  null=True,)
    caption = models.TextField(max_length=512, verbose_name='caption', null=True)
    is_active = models.BooleanField(default=True, verbose_name='active', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title


class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment', null=True, blank=True,verbose_name='post')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user',verbose_name='user')
    text = models.TextField(max_length=512,verbose_name='text')
    is_provide = models.BooleanField(default=True,verbose_name='provide')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
