from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


    #Custom validation
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({'Error': 'Age must be greater then 18'}) 
    
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'Error': 'Name cannot numaric'})

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = "__all__"
        # depth = 1
