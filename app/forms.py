from django import forms
from app.models import *
class StudentForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(max_value=35)

class BheemaGFForm(forms.ModelForm):
    class Meta:
        model=BheemaGF
        fields='__all__'