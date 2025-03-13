from django.db import models

# What is models?
# How dose the models page work

class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y%m%d')
    actaive = models.BooleanField(default=True)
    
    