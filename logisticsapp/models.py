from django.db import models

# Create your models here.
class quote(models.Model):
    departure = models.CharField(max_length=100)
    Delivery = models.CharField(max_length=100)
    Weight = models.IntegerField()
    Dimensions = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

