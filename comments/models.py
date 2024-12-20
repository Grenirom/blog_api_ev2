from django.db import models

from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    