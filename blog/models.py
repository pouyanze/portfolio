from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    body = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    favorites = models.ManyToManyField(User, related_name='favorite_posts', blank=True)


    def __str__(self):
        return str(self.title)
