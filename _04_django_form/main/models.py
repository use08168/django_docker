from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authot = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')