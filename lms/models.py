from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    description = models.TextField(null=True, blank=True)
    pages = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    class Meta:
        ordering = ["-updated"]

    def __str__(self) -> str:
        return str(self.title)


class Category(models.Model):
    type = models.CharField(max_length=30)
    books = models.ManyToManyField(Book)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated"]

    def __str__(self) -> str:
        return str(self.type)
