from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=10000)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')