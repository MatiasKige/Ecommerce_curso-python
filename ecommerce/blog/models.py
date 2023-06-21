from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    creation_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=30)
