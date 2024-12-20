from django.db import models

from category.models import Category


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post-images/', blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'{self.title}'
    