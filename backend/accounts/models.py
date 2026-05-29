from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)   # NEW

    room_number = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name