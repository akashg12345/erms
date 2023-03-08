from django import forms
from .models import EmployeeCreate

class EmployeeForm(forms.ModelForm):

    class Meta :
        model = EmployeeCreate
        fields = ["FirstName","LastName","Email",]
