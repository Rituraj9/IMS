from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/', views.job_search_list, name='job-search-list'),
    path('job/<slug>', views.job_detail, name='job-detail'),
    path('profile/', views.my_profile, name='my-profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('delete_skills/', views.delete_skill, name='skill-delete'),
    path('profile/<slug>', views.profile_view, name='profile-view'),
    path('job/<slug>/save/', views.save_job, name='save-job'),
    path('saved_job_list/', views.saved_jobs, name='saved-jobs'),
    path('job/<slug>/apply/', views.apply_job, name='apply-job'),
    path('applied_job_list/', views.applied_jobs, name='applied-jobs'),
    path('job/<slug>/remove/', views.remove_job, name='remove-job'),
   
]
