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
from management.models import recruiter_details,Candidate
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import uuid
from django.conf import settings
from django.core.mail import send_mail
#from .tokens import account_activation_token
from django.core.mail import EmailMessage
# Create your views here.

# Qwerty100@   password 4ni18is005 ka
def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account https://internmanagementsystem.herokuapp.com/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def  home(request):
    return render(request,'management/home.html')

def candidate_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name='candidate').exists():
        return render(request,'candidates/candidate_dashboard.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            profile_obj = Candidate.objects.filter(user = user ).first()
            if not profile_obj.is_verified:
                messages.success(request, 'Profile is not verified check your mail.')
                return render(request, 'management/candidate_login.html', {'form': form})

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
            email = form.cleaned_data.get('email')

            

            #if User.objects.filter(username = username).first():
            #    messages.success(request, 'Username is taken.')
            #    return render(request, 'management/candidate_register.html', {'form': form})

            #user_obj = User(username = username , email = email)
            #user_obj.set_password(raw_password)
            #user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Candidate.objects.create(user = user , auth_token = auth_token)
            profile_obj.save()
            print(email)
            send_mail_after_registration(email , auth_token)
            return redirect('token_send')

            #user = authenticate(username=username, password=raw_password)
            #ogin(request, user)
            #return redirect('http://127.0.0.1:8000/candidate/candidate_login/')

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

    return redirect('https://internmanagementsystem.herokuapp.com/')       

def success(request):
    return render(request , 'management/success.html')

def token_send(request):
    return render(request , 'management/token_send.html')

def verify(request , auth_token):
    try:
        profile_obj = Candidate.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('candidate_login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('candidate_login')
        else:
            return redirect('error_page')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'management/error.html')
