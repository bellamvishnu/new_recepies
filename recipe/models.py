from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingre = models.CharField(max_length=100)
    process = models.CharField(max_length=100)

    def __str__(self):
        return self.name
