from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.models import User


class recruiter_details(models.Model):
    username=models.CharField(max_length=30,blank=False , help_text='*required')
    company_name = models.CharField(max_length=30, blank=False, help_text='*required')
    est_year = models.CharField(max_length=4, blank=False, help_text="*required")
    hr_name = models.CharField(max_length=30, blank=False, help_text='*required')
    hr_phn = models.CharField(max_length=10,validators=[MinValueValidator(10),MaxValueValidator(10)], blank=False, help_text='*required')
    headquaters = models.CharField(max_length=30,blank=False, help_text='*required')
    about = models.CharField(max_length=1000, blank=False, help_text='*required')
    #type = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254,blank=False, help_text='Required. Inform a valid email address.')

    def __str__(self):
        return self.username


  


