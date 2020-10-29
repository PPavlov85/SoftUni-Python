from django.db import models


class Pet(models.Model):
    CAT = "cat"
    DOG = "dog"
    PARROT = "parrot"

    PET_TYPES = (
        (CAT, "Cat"),
        (DOG, "Dog"),
        (PARROT, "Parrot")
    )

    type = models.CharField(max_length=6, choices=PET_TYPES)
    name = models.CharField(max_length=6)
    age = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.name}"


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
