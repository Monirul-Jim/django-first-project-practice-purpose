from django import forms
from . import models


class StudentModelForms(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['roll']
        labels = {
            'name': 'Student Name',
            'roll': "Student Roll"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'})
        }
        # help_texts = {
        #     'name': "Write your full text"
        # }
        error_messages = {
            'name': {
                'required': 'Your name is required',
            },
            'roll': {
                'required': 'Student roll number is required',
                'invalid': 'Enter a valid roll number'
            }
        }
