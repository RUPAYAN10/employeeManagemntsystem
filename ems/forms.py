from django import forms
from ems.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = "__all__"
