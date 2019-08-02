from django.db import models

# Create your models here.


class baseLeaders(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False)
    phone_number=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.Name
