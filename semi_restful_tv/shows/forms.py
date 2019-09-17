from django import forms

class Add_Show_Form(forms.Form):
    Add_Show_Form = forms.CharField(label='Add Show', max_length=100)