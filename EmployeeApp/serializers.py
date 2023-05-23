from rest_framework import serializers
from EmployeeApp.models import *
from django.utils import timezone
import datetime
# from EmployeeApp.models import Departments, Employee, EmployeeDepartment,teacher,Province,City,Person,ItEmployee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields =('DepartmentId', 'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =('EmployeeId', 'EmployeeName', 'Department','DateOfJoined','PhotoFileName','DepartmentId')

class EmployeeDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDepartment
        fields = ('id', 'Departmentid', 'Employeeid')

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = ('id', 'teacherName','age','country')

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields= ('name')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'province')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('firstName', 'lastName','visitation','hometown','living')

class ItEmployeeSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    # name = serializers.SerializerMethodField()
    class Meta:
        model = ItEmployee
        fields = ('id', 'name','dateOfBirth','age')

    def get_age(self, instance):
        return timezone.now().year - instance.dateOfBirth.year

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
