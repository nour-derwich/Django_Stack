from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(default="testyhedcbfiehf")
	imgae = models.TextField(default="https://www.chappellegardensra.com/app/uploads/2023/01/book-club-1-2.jpg")
	number_page=models.IntegerField(default=100)
	type = models.TextField(default="Dev")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Auther(models.Model):
	name = models.CharField(max_length=255)
	notes=models.TextField()
	books = models.ManyToManyField(Book, related_name="auther_books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

