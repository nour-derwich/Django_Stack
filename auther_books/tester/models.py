from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Auther(models.Model):
	name = models.CharField(max_length=255)
	notes=models.TextField()
	books = models.ManyToManyField(Book, related_name="auther_books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

