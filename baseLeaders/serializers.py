from rest_framework import serializers
from .models import baseLeaders


class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model=baseLeaders
        fields=('id','Name','Email','date','phone_number')
