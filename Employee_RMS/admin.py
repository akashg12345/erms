from django.contrib import admin
from .models import EmployeeCreate, EmployeeEducation1, StudentResult

admin.site.register([EmployeeCreate,EmployeeEducation1,StudentResult])
