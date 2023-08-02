from django.db import models

# Create your models here.

    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    genre= models.TextField(default="darma")
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class User(models.Model):
    fullname = models.CharField(max_length=255)
    moves=models.ManyToManyField(Movie,related_name="uesers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "T"
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


