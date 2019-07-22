from django.db import models
import uuid

# Create your models here.

class Rider(models.Model):
	Name = models.CharField(max_length=300)
	IDNo = models.IntegerField(primary_key=True )
	DateofBirth = models.DateField(max_length=800)
	Gender = models.CharField(max_length=100)
	CountryCode = models.CharField(max_length=40)
	PhoneNumber = models.IntegerField()
	County = models.CharField(max_length=100)
	SubCounty = models.CharField(max_length=100)
	Ward = models.CharField(max_length=100)
	BaseName = models.CharField(max_length=100)
	YearsOfExperience = models.IntegerField()

	def __str__(self):
		return self.Name


class Vehicle(models.Model):
	Name = models.CharField(max_length=300)
	IDNo = models.ForeignKey(Rider, on_delete=models.CASCADE)
	FrameNumber= models.CharField(max_length=200)
	Make = models.CharField(max_length=200)
	RegNumber = models.CharField(max_length=100 ,primary_key=True)
	Ownership = models.CharField(max_length=100)

	def __str__(self):
		return self.FrameNumber


class Owner(models.Model):
	Name = models.CharField(max_length=300)
	IDNo  = models.CharField(max_length=200, blank=True, null=True)
	RegNumber = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	# FrameNumber= models.CharField(max_length=200)
	PhoneNumber = models.IntegerField()
	
	

	def __str__(self):
		return self.Name

class Insurance(models.Model):
	Name = models.CharField(max_length=300)
	IDNo = models.ForeignKey(Vehicle,  on_delete=models.CASCADE)
	Registration = models.CharField(max_length=100)
	InsuranceCompany = models.CharField(max_length=10,blank = True)
	InsuranceExpiry = models.DateField(max_length=8,blank = True)
	LicenseNumber = models.CharField(max_length=100)
	# PhoneNumber = models.IntegerField(max_length=100)
	
	def __str__(self):
		return self.Name


class Sacco(models.Model):
	Name = models.CharField(max_length=300)
	IDNo = models.ForeignKey(Rider,  on_delete=models.CASCADE)
	Membership = models.CharField(max_length=100)
	SaccoName = models.CharField(max_length=4,blank = True)
	DailyContribution = models.IntegerField()
	# PhoneNumber = models.IntegerField(max_length=100)
	
	def __str__(self):
		return self.Name

class myUser(models.Model):
	userID=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

		
