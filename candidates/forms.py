from django import forms
from .models import Profile, Skill


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'location',
                  'resume', 'institute', 'grad_year', 'looking_for','country',]


class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
