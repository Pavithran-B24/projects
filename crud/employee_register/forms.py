from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name','email','mobile','jobrole')
        labels ={
            
            'name' : 'Full Name',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['jobrole'].empty_label = 'Choose'
        self.fields['mobile'].required = False