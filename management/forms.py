from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms.widgets import DateInput,CheckboxSelectMultiple
from django.http import request




class candidate_SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='*required')
    last_name = forms.CharField(max_length=30, required=True, help_text='*required')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1', 'password2', )
        widgets={'dob':DateInput(attrs={'type':'date'})}


class recruiter_SignUpForm(UserCreationForm):
    recruiter_name = forms.CharField(max_length=30, required=True, help_text='*required')
    est_year=forms.CharField(max_length=4,required=True,help_text="*required")
    hr_name=forms.CharField(max_length=30, required=True, help_text='*required')
    hr_phn=forms.CharField(max_length=10, min_length=10,required=True, help_text='*required')
    headquaters=forms.CharField(max_length=30, required=True, help_text='*required')
    about=forms.CharField(max_length=1000, required=True, help_text='*required')
   
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'recruiter_name', 'est_year','hr_name','hr_phn','headquaters','about','email','password1', 'password2', )

    