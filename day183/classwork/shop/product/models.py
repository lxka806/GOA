from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    