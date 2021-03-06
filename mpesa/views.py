from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . models import Mpesa
from . serializers import MpesaSerializer
from . lipanampesa import lipa_na_mpesa

# Create your views here.
print("mpesa initialization")
@csrf_exempt
def mpesa_list(request):
    """"
    List  all mpesa calls
    """
    if request.method =="GET":
        print("READING MPESA")
        mpesas=Mpesa.objects.all()
        serializer=MpesaSerializer(mpesas,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method =="POST":
        print("MAKING MPESA PAYMENT")
        data = JSONParser().parse(request)
        print("DATA FOR PAYMENTS {}".format(data))
        serializer=MpesaSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            phone_no=data['phone_number']
            amount=data['amount']
            payBill=data['payBill']
            accref=data['accref']
            # here we run the function
            print("about to run the mpesa function")
            lipa_na_mpesa(phone_no,amount,payBill,accref)
            # end of function
            """
            serializer.save()
            """
            print("The data is :",data)
            print(request)
            return JsonResponse(serializer.data, status=201)
        else:
            print("Some shit went wrong!")
        return JsonResponse (serializer.errors, status=400)

