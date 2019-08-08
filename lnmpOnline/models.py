from django.db import models

# Create your models here.
class LnmpOnline(models.Model):
    checkoutRequestID= models.CharField(max_length=200)
    merchantRequestID= models.CharField(max_length=200)
    resultCode=models.IntegerField()
    resultDesc= models.CharField(max_length=200)
    amount=models.FloatField()
    mpesaReceiptNumber=models.CharField(max_length=50)
    transactionDate=models.DateTimeField()
    phoneNumber= models.CharField(max_length=15)
    accountRefId=models.CharField(max_length=100)
    accountRef=models.CharField(max_length=100)
    payBill=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.phoneNumber} has sent {self.amount} >> {self.mpesaReceiptNumber}"
