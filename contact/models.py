from django.db import models

# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    message = models.TextField()
