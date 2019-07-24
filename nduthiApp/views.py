from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Rider,Owner,Sacco,Insurance,Vehicle
from .serializers import RiderSerializer,VehicleSerializer,OwnerSerializer,SaccoSerializer,InsuranceSerializer
# Create your views here.
@csrf_exempt
def rider_list(request):

    if(request.method == 'GET'):
        riders=Rider.objects.all()
        serializer=RiderSerializer(riders,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        # mydata={'message': 'Hello, world!'}
        data=JSONParser().parse(request)
        serializer=RiderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Nicce")
            myres="hahaha"
            
            return JsonResponse(serializer.data, status=201)
            # return JsonResponse(data={'message': 'Hello, world!'})
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def owner_list(request):

    if(request.method == 'GET'):
        owners=Owner.objects.all()
        serializer=OwnerSerializer(owners,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        # mydata={'message': 'Hello, world!'}
        data=JSONParser().parse(request)
        serializer=OwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Nicce")
            myres="hahaha"
            
            return JsonResponse(serializer.data, status=201)
            # return JsonResponse(data={'message': 'Hello, world!'})
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def vehicle_list(request):

    if(request.method == 'GET'):
        vehicles=Vehicle.objects.all()
        serializer=VehicleSerializer(vehicles,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        # mydata={'message': 'Hello, world!'}
        data=JSONParser().parse(request)
        serializer=VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Nicce")
            myres="hahaha"
            
            return JsonResponse(serializer.data, status=201)
            # return JsonResponse(data={'message': 'Hello, world!'})
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def insurance_list(request):

    if(request.method == 'GET'):
        insurance=Insurance.objects.all()
        serializer=InsuranceSerializer(insurance,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        # mydata={'message': 'Hello, world!'}
        data=JSONParser().parse(request)
        serializer=InsuranceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Nicce")
            myres="hahaha"
            
            return JsonResponse(serializer.data, status=201)
            # return JsonResponse(data={'message': 'Hello, world!'})
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def sacco_list(request):

    if(request.method == 'GET'):
        saccos=Sacco.objects.all()
        serializer=SaccoSerializer(saccos,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        # mydata={'message': 'Hello, world!'}
        data=JSONParser().parse(request)
        serializer=SaccoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Nicce")
            myres="hahaha"
            
            return JsonResponse(serializer.data, status=201)
            # return JsonResponse(data={'message': 'Hello, world!'})
        return JsonResponse(serializer.errors, status=400)
