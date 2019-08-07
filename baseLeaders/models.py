from django.db import models
from django.utils import timezone

# Create your models here.


class BaseLeaders(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    date=models.DateField(default=timezone.now)
    phone_number=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.Name
