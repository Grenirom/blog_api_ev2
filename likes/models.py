from django.db import models

from post.models import Post


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='likes'    
    )


class Favorite(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='favorites'    
    )