from django.db import models

# What is models?
# How dose the models page work

class Car(models.Model):
        name= models.CharField(max_length=100)
        price = models.DecimalField(max_digits=6, decimal_places=2)
