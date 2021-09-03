from django import forms
from Testapp.models import Student

class DateInput(forms.DateInput):
    input_type = 'date'


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets = {
            'date': DateInput(),
        }
