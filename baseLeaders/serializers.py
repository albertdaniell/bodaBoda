from rest_framework import serializers
from .models import BaseLeaders,Base


class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model=BaseLeaders
        fields=('id','Name','Email','phone_number','password')



class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Base
        fields=('id','Name','base_leader')