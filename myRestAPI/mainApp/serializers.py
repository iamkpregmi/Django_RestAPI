from rest_framework import serializers
from  .models import Employee

#Create a Serializers Class
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

