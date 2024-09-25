from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    book_type = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=book_type)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
