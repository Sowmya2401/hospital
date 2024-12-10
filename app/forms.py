from django import forms
from . models import Booking
from django.forms import TextInput, Select, DateInput, Textarea

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = ['p_name','p_email','p_phone','p_department','p_doctor','p_date','p_msh']
        widgets={
            'p_name': TextInput(attrs={
                "name":"name",
                "type":"text",
                "placeholder":"Name"
            }),
            'p_email':TextInput(attrs={
                "name":"email",
                "type":"email",
                "placeholder":"Email"
            }),
            'p_phone':TextInput(attrs={
                "name":"phone",
                "type":"text",
                "placeholder":"Phone"
            }),
             'p_department': TextInput(attrs={
                "name":"department",
                "type":"text",
                "placeholder":"Departments"
            }),
            'p_doctor': Select(attrs={
                "name":"doctor",
                "type":"text",
                "placeholder":"Doctor"
            }),
            'p_date': DateInput(attrs={
                "name":"date",
                "type":"date",
                "placeholder":"Date"
            }),
            'p_msh': Textarea(attrs={
                "name":"msh",
                "placeholder":"Message"
            })
          
        }