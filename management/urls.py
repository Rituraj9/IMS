from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('recruiter/recruiter_login/', views.recruiter_login, name='recruiter_login'),
    path('candidate/candidate_login/', views.candidate_login,name='candidate_login'),
    path('candidate/candidate_register/', views.candidate_register, name='candidate_register'),
    path('recruiter/recruiter_register/', views.recruiter_register, name='recruiter_register'),
    path('logout/', views.pagelogout, name='logout')
    
    

]