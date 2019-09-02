from django.shortcuts import render
from .models import BaseLeaders,Base
from .serializers import LeadersSerializer,BaseSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def leaders_list(request):
    """
    List all code leader, or register
    """
    if request.method == 'GET':
        leaders = BaseLeaders.objects.all()
        serializer = LeadersSerializer(leaders, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LeadersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@csrf_exempt
def leader_detail(request,Email):
    """
    Retrieve, update or delete leader.
    """
    try:
        leaders = BaseLeaders.objects.get(Email=Email)
    except BaseLeaders.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LeadersSerializer(leaders)
        return JsonResponse(serializer.data)
    


@csrf_exempt
def leader_detail2(request,id):
    """
    Retrieve, update or delete leader.
    """
    try:
        leaders = BaseLeaders.objects.get(id=id)
    except BaseLeaders.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LeadersSerializer(leaders)
        return JsonResponse(serializer.data)
        
    
    

@csrf_exempt
def base_detail2(request,base_leader):
    """
    Retrieve, update or delete leader.
    """
    try:
        bases = Base.objects.get(base_leader=base_leader)
    except Base.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BaseSerializer(bases)
        return JsonResponse(serializer.data)
    
    @csrf_exempt
def base_detail(request,id):
    """
    Retrieve, update or delete leader.
    """
    try:
        bases = Base.objects.get(id=id)
    except Base.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BaseSerializer(bases)
        return JsonResponse(serializer.data)
        

@csrf_exempt
def base_list(request):
    """
    List all bases, or register base
    """
    if request.method == 'GET':
        bases = Base.objects.all()
        serializer = BaseSerializer(bases, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def sacco_detail(request, IDNo_id):
#     """
#     Retrieve, update or delete a sacco.
#     """
#     try:
#         sacco = Sacco.objects.get(IDNo_id=IDNo_id)
#     except Sacco.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SaccoSerializer(sacco)
#         return JsonResponse(serializer.data)
   