from django.db import models


class Bikes(models.Model):
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.brand

