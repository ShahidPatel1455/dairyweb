from django.db import models

# Create your models here.
class Milk(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.TextField()
    messege = models.TextField()

    def __str__(self):
        return self.name
    

