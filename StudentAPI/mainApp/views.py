from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self, request):
        student_obj = Student.objects.all()
        serializers = StudentSerializer(student_obj, many=True)
        return Response({'Students': serializers.data})

    def post(self, request):
        serializers = StudentSerializer(data=request.data)
        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
        return Response({'Student': serializers.data, 'message': 'Your data is saved successfully'})
    
    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializers = StudentSerializer(student_obj, data=request.data, partial=True)
            if not serializers.is_valid():
                return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
            else:
                serializers.save()
            return Response({'Student': serializers.data, 'message': 'Your data is saved successfully'})
        except Exception as e:
            return Response({'message':'Invalid Id'})
    
    def delete(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id']) # /?id=2 
            print(student_obj)
            serializers = StudentSerializer(student_obj)
            student_obj.delete()
            return Response({'Student': serializers.data,'message':'Deleted Successfully'})
        except Exception as e:
            return Response({'message':'Invalid Id'})


#--------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    print(book_obj)
    serializers = BookSerializer(book_obj, many=True)
    return Response({'Books': serializers.data})

@api_view(['GET'])
def students(request):
    student_obj = Student.objects.all()
    serializers = StudentSerializer(student_obj, many=True)
    return Response({'Students': serializers.data})

@api_view(['GET'])
def single_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        serializers = StudentSerializer(student_obj)
        return Response({'Student': serializers.data})
    except Exception as e:
        return Response({'message':'Invalid Id'})

@api_view(['POST'])
def add_student(request):
    
    #Custom validation
    # if request.data['age']<18:
    #     return Response({'Error': 'Age must be greater then 18'})
    
    serializers = StudentSerializer(data=request.data)

    if not serializers.is_valid():
        return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
    else:
        serializers.save()
    return Response({'Student': serializers.data, 'message': 'Your data is saved successfully'})


@api_view(['PATCH'])
def edit_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)

        serializers = StudentSerializer(student_obj, data=request.data, partial=True)
        if not serializers.is_valid():
            return Response({'Error': serializers.errors, 'message':'Sonething went wrong'})
        else:
            serializers.save()
        return Response({'Student': serializers.data, 'message': 'Your data is saved successfully'})

    except Exception as e:
        return Response({'message':'Invalid Id'})


@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        serializers = StudentSerializer(student_obj)
        student_obj.delete()
        return Response({'Student': serializers.data,'message':'Deleted Successfully'})
    except Exception as e:
        return Response({'message':'Invalid Id'})


