from pyclbr import Class
from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoined = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
    DepartmentId = models.ForeignKey(Departments, null=True, on_delete=models.SET_NULL)

class EmployeeDepartment(models.Model):
    id = models.AutoField(primary_key=True)
    Departmentid = models.ForeignKey(Departments,on_delete=models.CASCADE)
    Employeeid = models.ForeignKey(Employee,on_delete=models.CASCADE)

class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacherName = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=50,null=True)

class Province(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=25)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    # def __unicode__(self):
    def __str__(self):
        return self.name

class Person(models.Model):
    firstName = models.CharField(max_length=10,null=True)
    lastName = models.CharField(max_length=10,null=True)
    visitation = models.ManyToManyField(City, related_name="visitor")
    hometown = models.ForeignKey(City,related_name="birth",on_delete=models.CASCADE)
    living = models.ForeignKey(City,related_name="citizen",on_delete=models.CASCADE)
    def __unicode__(self):
        return self.firstName + self.lastName

class ItEmployee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dateOfBirth = models.DateField()

    # def age(self):
    #     return timezone.now().year - self.dateOfBirth.year