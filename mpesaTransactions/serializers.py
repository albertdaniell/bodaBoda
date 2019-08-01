from .models import LnmpOnline2
from rest_framework import serializers

class LnmpOnline2Serializer(serializers.ModelSerializer):
    class Meta:
        model = LnmpOnline2
        fields = ['checkoutRequestID', 'merchantRequestID', 'resultCode', 'resultDesc', 'amount', 'mpesaReceiptNumber','transactionDate','phoneNumber']