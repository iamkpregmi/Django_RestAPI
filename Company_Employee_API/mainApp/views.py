from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CompanyAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        company_obj = Company.objects.all()
        serializers = CompanySerializer(company_obj, many=True)
        
        return Response({'Status':200, 'Companies':serializers.data})


@api_view(['POST'])
def RegisterUser(request):
        serializers = UserSerializer(data= request.data)
        
        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
            user = User.objects.get(username = serializers.data['username'])
            token_obj = Token.objects.get_or_create(user=user)

        return Response({'Employee': serializers.data, 'Token':str(token_obj),'message': 'Your data is saved successfully'})

#Company View
@api_view(['GET'])
def companies(request):
    company_obj = Company.objects.all()
    serializers = CompanySerializer(company_obj, many=True)
    
    return Response({'Status':200, 'Companies':serializers.data})


@api_view(['GET'])
def company(request,id):
    try:
        company_obj = Company.objects.get(id=id)
        serializers = CompanySerializer(company_obj)
        
        return Response({'Status':200, 'Companies':serializers.data})
    
    except Exception as e:
        return Response({'Status':402,'Message':'Invalid Id'})


@api_view(['POST'])
def add_company(request):
    serializers = CompanySerializer(data=request.data)

    if not serializers.is_valid():
        return Response({'Status':402,'Error': serializers.errors, 'message':'Sonething went wrong'})
    else:
        serializers.save()
    return Response({'Status':200,'Company': serializers.data, 'message': 'Your data is saved successfully'})


@api_view(['PUT'])
def edit_company(request,id):
    try:
        company_obj = Company.objects.get(id=id)

        serializers = CompanySerializer(company_obj, data=request.data, partial=True)
        if not serializers.is_valid():
            return Response({'Status':402,'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
        return Response({'Status':200,'Company': serializers.data, 'message': 'Your data is saved successfully'})

    except Exception as e:
        return Response({'Status':402,'message':'Invalid Id'})
    

@api_view(['DELETE'])
def delete_company(request,id):
    try:
        company_obj = Company.objects.get(id=id)
        serializers = CompanySerializer(company_obj)
        company_obj.delete()
        return Response({'Status':200,'Company': serializers.data,'message':'Deleted Successfully'})
    except Exception as e:
        return Response({'Status':402,'message':'Invalid Id'})


#--------------------------------------------------------------------------------------------
#Employee View
@api_view(['GET'])
def employees(request):
    employee_obj = Employee.objects.all()
    serializers = EmployeeSerializer(employee_obj, many=True)
    
    return Response({'Status':200, 'Employees':serializers.data})

@api_view(['GET'])
def employee(request,id):
    try:
        employee_obj = Employee.objects.get(id=id)
        serializers = EmployeeSerializer(employee_obj)
        
        return Response({'Status':200, 'Employee':serializers.data})
    
    except Exception as e:
        return Response({'Status':402,'Message':'Invalid Id'})


@api_view(['POST'])
def add_employee(request):
    serializers = EmployeeSerializer(data=request.data)

    if not serializers.is_valid():
        return Response({'Status':402,'Error': serializers.errors, 'message':'Sonething went wrong'})
    else:
        serializers.save()
    return Response({'Status':200,'Employee': serializers.data, 'message': 'Your data is saved successfully'})


@api_view(['PUT'])
def edit_employee(request,id):
    try:
        employee_obj = Employee.objects.get(id=id)

        serializers = EmployeeSerializer(employee_obj, data=request.data, partial=True)
        if not serializers.is_valid():
            return Response({'Status':402,'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
        return Response({'Status':200,'Employee': serializers.data, 'message': 'Your data is saved successfully'})

    except Exception as e:
        return Response({'Status':402,'message':'Invalid Id'})
    

@api_view(['DELETE'])
def delete_employee(request,id):
    try:
        employee_obj = Employee.objects.get(id=id)
        serializers = EmployeeSerializer(employee_obj)
        employee_obj.delete()
        return Response({'Status':200,'Employee': serializers.data,'message':'Deleted Successfully'})
    except Exception as e:
        return Response({'Status':402,'message':'Invalid Id'})
    

#Custom URL for know mployee of Company
@api_view(['GET'])
def companyEmployee(request, id):
    try:
        company_obj = Company.objects.get(id=id)
        emp_name = Employee.objects.filter(Company_Name=company_obj)
        serializer = EmployeeSerializer(emp_name, many=True)
        return Response({'status': 200, 'Employees Data': serializer.data})
    
    except Company.DoesNotExist:
        return Response({'status': 404, 'error': 'Company not found'})
    except Employee.DoesNotExist:
        return Response({'status': 404, 'error': 'Employee data not found'})
    

