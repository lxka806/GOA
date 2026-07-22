from django.db import models

# Create your models here.
class BMW(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)

    