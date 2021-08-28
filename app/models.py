from django.db import models

# Create your models here.

class Main(models.Model):
    title = models.CharField( max_length=250)

    def __str__(self):
        return self.title 
    