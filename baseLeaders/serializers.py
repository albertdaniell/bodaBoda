from rest_framework import serializers
from .models import baseLeaders


class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model=baseLeaders
        fields=('Name','Email','date','phone_number')
