from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    thumbnails = models.ImageField(upload_to = 'thumbnails')
    categories = models.ManyToManyField(Categories)
    publish = models.BooleanField()
    read_time = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return self.title