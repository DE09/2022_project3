from django import forms
from .models import lohandsoft

class lohandsoftForm(forms.ModelForm):

    class Meta:
        model = lohandsoft
        fields = ('fullname', 'birth', 'email', 'age')
        labels = {
            'fullname':'Full Name',
            'birth':'Birth'
        } 
