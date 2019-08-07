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
        # convert to json
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



# Details views


@csrf_exempt
def rider_detail(request, pk):
    """
    Retrieve, update or delete a code rider.
    """
    try:
        riders = Rider.objects.get(pk=pk)
    except Rider.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RiderSerializer(riders)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RiderSerializer(riders, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        riders.delete()
        return HttpResponse(status=204)
    
    
    
@csrf_exempt
def owner_detail(request, FrameNumber):
    """
    Retrieve, update or delete a code owner.
    """
    try:
        owners = Owner.objects.get(FrameNumber=FrameNumber)
    except Owner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OwnerSerializer(owners)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OwnerSerializer(owners, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        owners.delete()
        return HttpResponse(status=204)
    

@csrf_exempt
def vehicle_detail(request, IDNo_id):
    """
    Retrieve, update or delete a vehicle.
    """
    try:
        vehicle = Vehicle.objects.get(IDNo_id=IDNo_id)
    except Vehicle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(vehicle, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vehicle.delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def insurance_detail(request, FrameNumber):
    """
    Retrieve, update or delete a code owner.
    """
    try:
        insurance = Insurance.objects.get(FrameNumber=FrameNumber)
    except Insurance.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InsuranceSerializer(insurance)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InsuranceSerializer(insurance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        insurance.delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def sacco_detail(request, IDNo_id):
    """
    Retrieve, update or delete a sacco.
    """
    try:
        sacco = Sacco.objects.get(IDNo_id=IDNo_id)
    except Sacco.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SaccoSerializer(sacco)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SaccoSerializer(sacco, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sacco.delete()
        return HttpResponse(status=204)