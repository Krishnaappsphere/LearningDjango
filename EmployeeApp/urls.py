from django.urls import include, path
# from EmployeeApp import views as view
# from views import departmentApi
# from django.conf.urls import url
from . import views
from django.urls import include, re_path
from rest_framework import routers
from EmployeeApp.views import *
from rest_framework.routers import SimpleRouter,DefaultRouter
# from EmployeeApp.views import departmentApi,employeeApi,employeeDepartmentApi,testing,join_list,teacherApi,selectRelated, itemployeeApi


from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('dep',depViewset)

poll_list_view = depViewset.as_view({
    "get": "list",
    "post": "create"
})


urlpatterns = [
    path('',include(router.urls)),
    # re_path('dep', departmentApi, name='departmentApi'),
    # #Url for edit and delete department data
    # path('dep/<int:id>',views.departmentApi,name='departmentApi'),
    re_path('emp', employeeApi, name='employeeApi'),
    #Url for edit and delete employee data
    path('emp/<int:id>', views.employeeApi, name='employeeApi'),
    re_path('empdep', employeeDepartmentApi, name='employeeDepartmentApi'),
    # re_path('list', NameList, name='NameList')
    path('testing/', views.testing,
         name="testing"),
    path('join_list',views.join_list, name='join_list'),
    path('teacher', views.teacherApi, name='teacherApi'),
    path('teacher/<int:id>', views.teacherApi, name='teacherApi'),
    path('selectRelated/', views.selectRelated, name='selectRelated'),
    path('cool/', views.itemployeeApi, name = 'itemployeeApi'),
    path('cool/<int:id>/edit', views.itemployeeApi, name = 'itemployeeApi'),
    path('getage',views.getAge, name='getage'),
    # path('upd',views.updateData, name = 'updateData'),
]
# urlpatterns=[
#     path("index/", view.departmentApi, name="main-view"),
#     url('^department/([0-9]+)$',views.departmentApi),
#     # url(r'^department',include(views.departmentApi))

#     url(r'^employee$',views.employeeApi),
#     url(r'^employee/([0-9]+)$',views.employeeApi),

#     url(r'^employee/savefile',views.SaveFile)
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#middlewares
#re_path
#routing