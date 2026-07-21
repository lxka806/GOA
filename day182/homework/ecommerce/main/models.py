from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
