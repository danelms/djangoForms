from django.db import models
from django.db.models.deletion import CASCADE

class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
            return self.title

class Pizza(models.Model):
    topping1 = models.CharField(max_length=50)
    topping2 = models.CharField(max_length=50)
    size = models.ForeignKey(Size, on_delete=CASCADE)

