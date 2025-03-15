from django.db import models

# What is models?
# How dose the models page work


class Login(models.Model):
   
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username