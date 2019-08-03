from django.shortcuts import render
from .models import baseLeaders
from .serializers import LeadersSerializer
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
        leaders = baseLeaders.objects.all()
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
        leaders = baseLeaders.objects.get(Email=Email)
    except baseLeaders.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LeadersSerializer(leaders,many=True)
        return JsonResponse(serializer.data , safe=False)

   