from django.db import models


class FoodMenu(models.Model):
    day = models.CharField(max_length=20)
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return self.day