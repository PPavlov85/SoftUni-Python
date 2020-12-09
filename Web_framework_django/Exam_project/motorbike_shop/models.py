from django.db import models


class Bikes(models.Model):
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    image = models.ImageField(upload_to="bike_images",)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id}/ {self.model}/ {self.brand}"

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Bikes, self).delete(*args, **kwargs)
        storage.delete(path)
