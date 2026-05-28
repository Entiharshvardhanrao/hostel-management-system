from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    room_number = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name