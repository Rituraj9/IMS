from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import candidate_SignUpForm,recruiter_SignUpForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from management.models import recruiter_details
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# Create your views here.

# Qwerty100@   password 4ni18is005 ka
def  home(request):
    return render(request,'management/home.html')

def candidate_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name='candidate').exists():
        return render(request,'candidates/candidate_dashboard.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.groups.filter(name='candidate').exists():
             return render(request, 'candidates/candidate_dashboard.html', {'form': form})
            else:
                logout(request)
                return render(request, 'management/candidate_login.html', {'form': form})
        else:
            return render(request, 'management/candidate_login.html', {'form': form})


    else:
        form = AuthenticationForm()
        return render(request, 'management/candidate_login.html', {'form': form})


def candidate_register(request):
    if request.method == 'POST':
        form = candidate_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='candidate')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/candidate/candidate_login/')

        else:
            return render(request, 'management/candidate_register.html', {'form': form})
    else:
        form =candidate_SignUpForm()
        return render(request, 'management/candidate_register.html', {'form': form})

def recruiter_register(request):
    if request.method == 'POST':
        form = recruiter_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='recruiter')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            a=recruiter_details()
            a.username=request.POST.get('username')
            a.recruiter_name=request.POST.get('recruiter_name')
            a.email=request.POST.get('email')
            a.est_year=request.POST.get('est_year')
            a.about=request.POST.get('about')
            a.hr_name=request.POST.get('hr_name')
            a.hr_phn=request.POST.get('hr_phn')
            a.headquaters=request.POST.get('headquaters')
            a.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('recruiter_login')
        else:
            return render(request, 'management/recruiter_register.html', {'form': form})
    else:
        form = recruiter_SignUpForm()
        return render(request, 'management/recruiter_register.html', {'form': form})       

def recruiter_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name='recruiter').exists():
        return render(request,'recruiters/hiring.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.groups.filter(name='recruiter').exists():
                #print("Success")
                return render(request, 'recruiters/hiring.html', {'form': form})
            else:
                logout(request)
                return render(request, 'management/recruiter_login.html', {'form': form})
        else:
            return render(request, 'management/recruiter_login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'management/recruiter_login.html', {'form': form})

def pagelogout(request):
    logout(request)

    return redirect('http://127.0.0.1:8000/')       
