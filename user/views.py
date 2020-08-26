from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm 
from django.template.loader import get_template 
from django.template import Context 
from django.utils import timezone

from .models import Delegate

#################### index#######################################  
def index(request): 
    return render(request, 'user/index.html', {'title':'index'}) 

########### register here #####################################  
def register(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            email = form.cleaned_data.get('email') 
            phone = form.cleaned_data.get('phone_no')
            Fname = form.cleaned_data.get('first_name')
            Lname = form.cleaned_data.get('last_name')

            ######################### mail system ####################################  
            htmly = get_template('user/Email.html') 
            d = { 'username': username } 
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email 
            html_content = htmly.render(d) 
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            #msg.attach_alternative(html_content, "text/html") 
            #msg.send() 
            ##################################################################  
            messages.success(request, f'Your account has been created ! You are now able to log in') 
            newUser = Delegate(name=username, join_date=timezone.now(), first_name=Fname ,last_name = Lname,acheivement="none")
            newUser.save()
            return redirect('login') 
    else: 
        form = UserRegisterForm() 
    return render(request, 'user/register.html', {'form': form, 'title':'register here'}) 
   
################ login forms###################################################  
def Login(request): 
    if request.method == 'POST': 
   
        # AuthenticationForm_can_also_be_used__ 
   
        username = request.POST['username'] 
        password = request.POST['password'] 
        
        user = authenticate(request, username=username, password=password) 
        if user is not None: 
            form = login(request, user) 
            messages.success(request, f' welcome {username} !!') 
            url = 'user/' + username
            
            return redirect(url) 
        else: 
            messages.info(request, f'Account does not exist. Please try again') 
    form = AuthenticationForm() 
    return render(request, 'user/login.html', {'form': form, 'title':'log in'}) 

"""
    NEW LOGGED IN FUNCTION WHICH SENDS TO PROFILE PAGE OF THE USER
"""
def loggedin(request, username):
    d = Delegate.objects.get(name=username)  
    date_joined = d.join_date
    acheivements = d.acheivement
    fname = d.first_name
    lname = d.last_name
    name = fname + ' ' + lname
    throw_to_frontend ={
        'title': 'Profile',
        'name' : name,
        'username': username,
        'join_date': date_joined,
        'acheivement': acheivements,
    }

    return render(request, 'user/profile.html', throw_to_frontend)


def password_change(request):

    return render(request, 'user/change_password.html', {'title':'MUnite'})