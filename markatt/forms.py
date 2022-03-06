from calendar import c
from django import forms

Attendance_Status = [('A','A'),('P','P')]

class Attform(forms.Form):
    status = forms.CharField(widget=forms.RadioSelect(choices=Attendance_Status))

 