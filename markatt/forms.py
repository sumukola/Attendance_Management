from calendar import c
from django import forms

class Attform(forms.Form):
    _ = forms.CharField(widget=forms.CheckboxInput(),required=False)