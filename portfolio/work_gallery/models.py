from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='works')
    date = models.DateField(auto_now_add=True)
