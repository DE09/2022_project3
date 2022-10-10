from django import forms
from .models import lohandsoft, employee_list

class lohandsoftForm(forms.ModelForm):

    class Meta:
        model = lohandsoft
        fields = ('fullname', 'birth', 'email', 'age')
        labels = {
            'fullname':'Full Name',
            'birth':'Birth'
        } 

class employee_listForm(forms.ModelForm):

    class Meta:
        model = employee_list
        fields = ('employee_id', 'employee_pass')
        labels = {
            'employee_id':'Employee_ID',
            'employee_pass':'Employee_PASS'
        }