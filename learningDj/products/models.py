from django.db import models

# migration mean put this class in django files => python manage.py makemigrations
# migrate mean put in db => python manage.py migrate

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y%m%d')
    actaive = models.BooleanField(default=True)
    