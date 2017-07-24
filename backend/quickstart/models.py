from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    publish_time = models.DateTimeField()
    content = models.TextField()