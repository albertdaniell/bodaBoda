from django.db import models
from django.utils import timezone
import uuid 

# Create your models here.


class BaseLeaders(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150,unique=True)
    date=models.DateField(default=timezone.now)
    phone_number=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    def __str__(self):
        return self.Name
    
class Base(models.Model):
    Name=models.CharField( max_length=200)
    date=models.DateField(default=timezone.now)
    base_leader=models.ForeignKey(BaseLeaders, on_delete=models.CASCADE)
    base_code=models.UUIDField(unique=True ,default=uuid.uuid4,)

