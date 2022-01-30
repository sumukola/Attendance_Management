from calendar import c
from django import forms

SEMS= [
    ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),]

Section = [('A','A'),('B','B'),('C','C')]

class Sem(forms.Form):
    SEMS = forms.CharField(widget=forms.RadioSelect(choices=SEMS))

class Sec(forms.Form):
    SEC = forms.CharField(widget=forms.RadioSelect(choices=Section))

class Sub(forms.Form):
    SUB = forms.CharField(label='sub',widget=forms.TextInput(attrs={'placeholder':'like DBMS/CN/CG'}),max_length=10,min_length=2) 