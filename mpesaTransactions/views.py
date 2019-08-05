from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from lnmpOnline.models import LnmpOnline
from .serializers import LnmpOnline2Serializer

# Create your views here.


@csrf_exempt
def payments(request):
    """
    List all paymets
    """
    if request.method == 'GET':
        payments = LnmpOnline.objects.all()
        serializer = LnmpOnline2Serializer(payments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer=MpesaSerializer(data=data)
        if serializer.is_valid():
            print(request.data)
        #     phone_no=data['phone_number']
        #     amount=data['amount']
        #     payBill=data['payBill']
        #     accref=data['accref']
        #     # here we run the function
        #     lipa_na_mpesa(phone_no,amount,payBill,accref)
        #     # end of function
        #     serializer.save()
        #     print("The data is :",data)
        #     print(request)
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse (serializer.errors, status=400)




@csrf_exempt
def payment_detail(request,phoneNumber):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        payments = LnmpOnline.objects.filter(phoneNumber=phoneNumber)
    except LnmpOnline.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LnmpOnline2Serializer(payments,many=True)
        return JsonResponse(serializer.data , safe=False)

   

  