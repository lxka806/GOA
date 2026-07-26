from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    age = models.IntegerField()
    is_curent_user = models.BooleanField(default=0)