from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()