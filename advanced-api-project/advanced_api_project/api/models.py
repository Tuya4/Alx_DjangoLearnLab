from django.db import models

# Create Author model that represents authors of books with 'name' as it's field
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create Book model that represents books published by authors with 'title', 'publication_year' and 'author' as it's fields    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # One-to-many relationship from Author to Books

    def __str__(self):
        return f"{self.title} by {self.author}"  

    # class Meta:
    #     ordering = ['-publication_year']  