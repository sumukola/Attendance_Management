from django import forms 

class stu_form(forms.Form):
    rollno = forms.IntegerField(max_value=100,min_value=1,required=True)
    usn = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'USN'}),max_length=10,required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}),required=True)
    
