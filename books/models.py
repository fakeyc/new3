from django.db import models

# Create your models here.
class books_to_read(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.TextField()
    image = models.FilePathField(path="/img")