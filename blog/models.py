from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
