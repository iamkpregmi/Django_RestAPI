from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company

def home(request):
    friends = [
        'Brijesh Mishara',
        'Rajneesh Kumar Shah',
        'Sapan Mitra',
        'Fayaz Alam',
        'Rohit Kumar Rana'
    ]
    return JsonResponse(friends,safe=False)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
