from lnmpOnline.models import LnmpOnline
from rest_framework import serializers

class LnmpOnline2Serializer(serializers.ModelSerializer):
    class Meta:
        model = LnmpOnline
        fields = ['checkoutRequestID', 'merchantRequestID', 'resultCode', 'resultDesc', 'amount', 'mpesaReceiptNumber','transactionDate','phoneNumber']