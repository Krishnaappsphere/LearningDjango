from django.shortcuts import render
# from EmployeeApp.task import send_email_fun
from DjangoApi import settings
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
import json as simplejson
# from django.views.generic import View
# from rest_framework.views import APIView
from rest_framework import viewsets
from datetime import date
# from django.utils import simplejson

from EmployeeApp.models import *
# from EmployeeApp.models import Departments,Employee, EmployeeDepartment,teacher,Province,City,Person, ItEmployee
from EmployeeApp.serializers import *
# from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer,EmployeeDepartmentSerializer,teacherSerializer,ProvinceSerializer,CitySerializer,PersonSerializer, ItEmployeeSerializer
from rest_framework.response import Response
from django.core.files.storage import default_storage

# Create your views here.
# @csrf_exempt
# def departmentApi(request,id=0):
#     if request.method=='GET':
#         departments = Departments.objects.all()
#         departments_serializer=DepartmentSerializer(departments,many=True)
#         return JsonResponse(departments_serializer.data,safe=False)
#     elif request.method=='POST':
#         department_data=JSONParser().parse(request)
#         departments_serializer=DepartmentSerializer(data=department_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         department_data=JSONParser().parse(request)
#         department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
#         departments_serializer=DepartmentSerializer(department,data=department_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         department=Departments.objects.get(DepartmentId=id)
#         department.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

class depViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()
    lookup_field = 'DepartmentId'

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employee = Employee.objects.all()
        employees_serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def employeeDepartmentApi(request,id=0):
    if request.method=='GET':
        employeeDepartment = EmployeeDepartment.objects.all()
        employeeDepartment_serializer=EmployeeDepartmentSerializer(employeeDepartment,many=True)
        return JsonResponse(employeeDepartment_serializer.data,safe=False)
    elif request.method=='POST':
        employeeDepartment_data=JSONParser().parse(request)
        employeeDepartment_serializer=EmployeeDepartmentSerializer(data=employeeDepartment_data)
        if employeeDepartment_serializer.is_valid():
            employeeDepartment_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employeeDepartment_data=JSONParser().parse(request)
        employeeDepartment=EmployeeDepartment.objects.get(id=employeeDepartment_data['id'])
        employeeDepartment_serializer=EmployeeDepartmentSerializer(employeeDepartment,data=employeeDepartment_data)
        if employeeDepartment_serializer.is_valid():
            employeeDepartment_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employeeDepartment=EmployeeDepartment.objects.get(id=id)
        employeeDepartment.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#Filter by departmenr Name
def testing(request):
  mydata = Departments.objects.filter(DepartmentName='IT').values()
  template = loader.get_template('show_details.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

#Join list
def join_list(request):
    department_employees = EmployeeDepartment.objects.select_related('Departmentid', 'Employeeid')
    # print(department_employees.query)
    datas = []
    for de in department_employees:
        # print(de.Departmentid.DepartmentName, de.Employeeid.EmployeeName)
        detail_dict =  {}
        detail_dict['DepartmentName'] = de.Departmentid.DepartmentName
        detail_dict['EmployeeName'] = de.Employeeid.EmployeeName

        datas.append(detail_dict)
    return HttpResponse(datas)


#teacher table
@csrf_exempt
def teacherApi(request,id=0):
    if request.method=='GET':
        teachers = teacher.objects.all()
        teacher_serializer=teacherSerializer(teachers,many=True)
        return JsonResponse(teacher_serializer.data,safe=False)
    elif request.method=='POST':
        teacher_data=JSONParser().parse(request)
        teacher_serializer=teacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='DELETE':
        teachers=teacher.objects.get(id=id)
        teachers.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#select_related
def selectRelated(request):
    if request.method=='GET':
        citys = City.objects.select_related().all().values('name')
        # print(citys)
        # for c in citys:
        #     print(c.province)
    return HttpResponse(citys)

@csrf_exempt
def itemployeeApi(request,id=0):
    if request.method=='GET':
        itemployee = ItEmployee.objects.all()
        itemployee_serializer=ItEmployeeSerializer(itemployee,many=True)
        return JsonResponse(itemployee_serializer.data,safe=False)
    elif request.method=='POST':
        itemployee=JSONParser().parse(request)
        itEmployee_Serializer=ItEmployeeSerializer(data=itemployee)
        if itEmployee_Serializer.is_valid():
            itEmployee_Serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        itemployee_data=JSONParser().parse(request)
        itemp=ItEmployee.objects.get(id=itemployee_data['id'])
        itemp_serializer=ItEmployeeSerializer(itemp,data=itemployee_data)
        if itemp_serializer.is_valid():
            itemp_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

#Get itEmployee age
@csrf_exempt
def getAge(request):
    if request.method=='GET':
        itemp = ItEmployee.objects.all()
        datesEmp =[]
        for dob in itemp:
            today = date.today()
            td = today.year - dob.dateOfBirth.year
            datesEmp.append(td)
        # print(datesEmp)
        json_stuff = simplejson.dumps({"Age" : datesEmp})
        return HttpResponse(json_stuff, content_type ="application/json")

# def send_email(request):
#     send_email_fun("Celery", "Success", settings.EMAIL_HOST_USER, "ksisodiya196@gmail.com")
#     return HttpResponse("Sent Email Successfully...Check your mail please")


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)