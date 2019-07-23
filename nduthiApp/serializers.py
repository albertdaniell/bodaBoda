from rest_framework import serializers
from .models import Rider,Owner,Sacco,Insurance,Vehicle

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rider
        fields=('Name','IDNo','DateofBirth','Gender','CountryCode','PhoneNumber','County','SubCounty','Ward','BaseName','YearsOfExperience')
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Owner
        fields=('id','Name','IDNo','FrameNumber','PhoneNumber')
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields=('Name','IDNo','FrameNumber','Make','RegNumber','Ownership')
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Insurance
        fields=('id','Name','FrameNumber','HasInsurance','InsuranceCompany','InsuranceExpiry','LicenseNumber')
class SaccoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sacco
        fields=('Name','IDNo','Membership','SaccoName','DailyContribution')