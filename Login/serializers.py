from rest_framework import serializers
from .models import * 

class EmployeeSerializer(serializers.ModelSerializer):
     class Meta:
        model = Employee
        fields = '__all__' 

class HRSerializer(serializers.ModelSerializer):
     class Meta:
        model = HR
        fields = '__all__' 