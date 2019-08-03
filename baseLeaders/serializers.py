from rest_framework import serializers
from .models import BaseLeaders


class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model=BaseLeaders
        fields=('id','Name','Email','date','phone_number')
