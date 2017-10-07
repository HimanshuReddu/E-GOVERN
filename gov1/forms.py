from django import forms
from django.contrib.auth.models import User
from .models import Complaint,Birth,Death

class ComplaintCreate(forms.ModelForm):
    class Meta:
        model=Complaint
        fields = ['username', 'email','number', 'complaint',]

        labels = {'username': 'UserName',
                  'email':'Email_ID',
                  'number':'Ph_Number',
                  'complaint':'Complaint',}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.TextInput(attrs={'class':'form-control'}),
                 'number':forms.TextInput(attrs={'class':'form-control'}),
                 'complaint':forms.TextInput(attrs={'class':'form-control'}),

        }

class BirthCreate(forms.ModelForm):
    class Meta:
        model=Birth
        fields = ['form_no', 'date', 'id_number', 'name', 'father', 'mother', 'dob', 'gender', 'occfather', 'occmother',
                  'birthplace', 'address', 'number', 'email']

        labels = {'form_no': 'Form_No',
                  'date':'Date_of_registration',
                  'id_number':'Id_Number',
                  'name':'Name',
                  'father': 'Father_Name',
                  'mother': 'Mother_Name',
                  'dob': 'dob',
                  'gender': 'Gender',
                  'occfather': 'Fathers_occupation',
                  'occmother': 'Mothers_occupation',
                  'birthplace': 'Birth_Place',
                  'address': 'Address',
                  'number': 'Contact_Number',
                  'email':'Email',}
        widgets={'form_no':forms.TextInput(attrs={'class':'form-control'}),
                 'date':forms.TextInput(attrs={'class':'form-control'}),
                 'id_number':forms.TextInput(attrs={'class':'form-control'}),
                 'name':forms.TextInput(attrs={'class':'form-control'}),
                 'father': forms.TextInput(attrs={'class': 'form-control'}),
                 'mother': forms.TextInput(attrs={'class': 'form-control'}),
                 'dob': forms.TextInput(attrs={'class': 'form-control'}),
                 'gender': forms.TextInput(attrs={'class': 'form-control'}),
                 'occfather': forms.TextInput(attrs={'class': 'form-control'}),
                 'occmother': forms.TextInput(attrs={'class': 'form-control'}),
                 'birthplace': forms.TextInput(attrs={'class': 'form-control'}),
                 'address': forms.TextInput(attrs={'class': 'form-control'}),
                 'number': forms.TextInput(attrs={'class': 'form-control'}),
                 'email': forms.TextInput(attrs={'class': 'form-control'}),
                        }


class BirthCreate(forms.ModelForm):
    class Meta:
        model = Death
        fields = ['form_no', 'date', 'id_number', 'name', 'father', 'mother', 'dob', 'ddate', 'gender',
                  'address', 'contact', 'email', 'cause']

        labels = {'form_no': 'Form_No',
                  'date': 'Date_of_registration',
                  'id_number': 'Id_Number',
                  'name': 'Name',
                  'father': 'Father_Name',
                  'mother': 'Mother_Name',
                  'dob': 'dob',
                  'gender': 'Gender',

                  'address': 'Address',
                  'contact': 'Contact_Number',
                  'email': 'Email',
                  'cause':'Cause_of_deathn h'}
        widgets = {'form_no': forms.TextInput(attrs={'class': 'form-control'}),
                   'date': forms.TextInput(attrs={'class': 'form-control'}),
                   'id_number': forms.TextInput(attrs={'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'father': forms.TextInput(attrs={'class': 'form-control'}),
                   'mother': forms.TextInput(attrs={'class': 'form-control'}),
                   'dob': forms.TextInput(attrs={'class': 'form-control'}),
                   'gender': forms.TextInput(attrs={'class': 'form-control'}),

                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'contact': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'cause   ': forms.TextInput(attrs={'class': 'form-control'}),
                   }


