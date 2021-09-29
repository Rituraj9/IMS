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
    
    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' , views.error_page , name="error"),
    
    path('logout/', views.pagelogout, name='logout'),
   # path('activate/<uidb64>/<token>', views.activate, name='activate')
    
    

]