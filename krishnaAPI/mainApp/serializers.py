from rest_framework import serializers
from .models import Company

#Create Serializer here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Company
        fields = "__all__"