from django import forms
from django.forms import fields
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "number")
        labels = {"first_name": "Your Name"}
        # widgets = {
        #     "first_name": forms.TextInput(attrs={"class": "form-control"}),
        #     "last_name": forms.TextInput(attrs={"class": "form-control"}),
        #     "number": forms.NumberInput(attrs={"class": "form-control"})
        # }
