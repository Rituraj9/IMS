from django import forms
from .models import Job

class DateInput(forms.DateInput):
    input_type = 'date'

class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'internship','stipend', 'date_of_join', 'link']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }
        widgets = {
            'date_of_join': DateInput(),
        }


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'internship','stipend','date_of_join','link']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }
        widgets = {
            'date_of_join': DateInput(),
        }
