from django.db import models
import uuid

# Create your models here.

class Rider(models.Model):
	Name = models.CharField(max_length=300)
	IDNo = models.IntegerField(primary_key=True )
	DateofBirth = models.CharField(max_length=800)
	Gender = models.CharField(max_length=100)
	CountryCode = models.CharField(max_length=40)
	PhoneNumber = models.CharField(max_length=100)
	County = models.CharField(max_length=100)
	SubCounty = models.CharField(max_length=100)
	Ward = models.CharField(max_length=100)
	BaseName = models.ForeignKey("baseLeaders.Base", on_delete=models.CASCADE)
	YearsOfExperience = models.IntegerField()

	def __str__(self):
		return self.Name


class Vehicle(models.Model):
	Name = models.CharField(max_length=300)
	IDNo = models.ForeignKey(Rider, on_delete=models.CASCADE)
	FrameNumber= models.CharField(max_length=200,primary_key=True)
	Make = models.CharField(max_length=200)
	RegNumber = models.CharField(max_length=100 )
	Ownership = models.CharField(max_length=100)

	def __str__(self):
		return self.FrameNumber


class Owner(models.Model):
	Name = models.CharField(max_length=300)
	IDNo  = models.CharField(max_length=200, blank=True, null=True)
	FrameNumber = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	# FrameNumber= models.CharField(max_length=200)
	PhoneNumber = models.CharField(max_length=100)
	
	

	def __str__(self):
		return self.Name

class Insurance(models.Model):
	Name = models.CharField(max_length=300)
	FrameNumber = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	HasInsurance = models.CharField(max_length=100, blank=True, null=True)
	# Registration = models.CharField(max_length=100)
	InsuranceCompany = models.CharField(max_length=10,blank = True,null=True)
	InsuranceExpiry = models.CharField(max_length=100,blank = True,null=True)
	LicenseNumber = models.CharField(max_length=100)
	# PhoneNumber = models.IntegerField(max_length=100)
	
	def __str__(self):
		return self.Name


class Sacco(models.Model):
	Name = models.CharField(max_length=300)
	IDNo = models.ForeignKey(Rider,  on_delete=models.CASCADE)
	Membership = models.CharField(max_length=100)
	SaccoName = models.CharField(max_length=100,blank = True,null=True)
	DailyContribution = models.CharField(max_length=300,blank = True,null=True)
	# PhoneNumber = models.IntegerField(max_length=100)
	
	def __str__(self):
		return self.Name

class myUser(models.Model):
	userID=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

		
