from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    book_title = models.CharField(max_length=100)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)

