from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    published_at = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title