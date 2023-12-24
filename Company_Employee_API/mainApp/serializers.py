from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

    #Custom validation
    def validate(self, data):
        if data['company_name']:
            for n in data['company_name']:
                if n.isdigit():
                    raise serializers.ValidationError({'Error': 'Company Name cannot numaric'})
        return data


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

