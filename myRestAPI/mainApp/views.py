from django.shortcuts import render
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import viewsets

def home(request):
    return render(request,"index.html")

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

