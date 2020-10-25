from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.template.loader import get_template
from django.template import Context
from django.utils import timezone

from .models import Delegate, Event

#################### index#######################################
def index(request):

    all_events = Event.objects.all()
    D=[]
    for i in all_events:
        organizer = i.core_organizer
        event = i.event
        organization = i.organization
        date = i.date
        venue = i.venue
        price = i.price
        L = (event, organization, date, venue, price, organizer)
        D.append(L)

    throw_to_frontend = {
        'events':D
    }
    return render(request, 'user/index.html', throw_to_frontend)


############ event registration saving in database ################################
def save_event(request):
    print(request.POST)
    #getting current logged in username
    username = request.user.get_username()
    #getting id of currently logged in username
    #id used in creating new Event object
    id = Delegate.objects.only('id').get(name=username).id
    event = request.POST.get('event')
    organization = request.POST.get('org')
    date = request.POST.get('date')
    venue = request.POST.get('venue')
    price = request.POST.get('price')
    description = request.POST.get('description')
    Event.objects.create(core_organizer_id=id, event=event,
    organization=organization, date=date, venue=venue, price=price, description=description)

    ##### showing index page with new events
    all_events = Event.objects.all()
    D = []
    for i in all_events:
        event = i.event
        organization = i.organization
        date = i.date
        venue = i.venue
        price = i.price
        des = i.description
        L = (event, organization, date, venue, price, des)
        D.append(L)

    throw_to_frontend = {
        'events': D
    }
    return render(request, 'user/index.html', throw_to_frontend)

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
            ###############
            messages.success(request, f'Your account has been created ! You are now able to log in')
            newUser = Delegate(name=username, rating=0 , join_date=timezone.now(), first_name=Fname ,last_name = Lname,acheivement="none")
            newUser.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})

###### login forms
#  
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__ 

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            ##url = 'user/' + username

            return redirect('/')
        else:
            messages.info(request, f'Account does not exist. Please try again')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title':'log in'})


########NEW LOGGED IN FUNCTION WHICH SENDS TO PROFILE PAGE OF THE USER ############

def loggedin(request, username):
    login = str(request.user)
    if username != login:
        canedit = 0
    else:
        canedit = 1

    d = get_object_or_404(Delegate, name=username)
    rating = d.rating
    date_joined = d.join_date
    acheivements = d.acheivement
    fname = d.first_name
    lname = d.last_name
    name = fname + ' ' + lname


    throw_to_frontend ={
        'title': 'Profile',
        'rating': rating,
        'name': name,
        'username': username,
        'join_date': date_joined,
        'acheivement': acheivements,
        'profile_pic': d.profile_pic,
        'edit':  canedit,
    }
    return render(request, 'user/profile.html', throw_to_frontend)

# Returning create_event page


def create_event(request, username):
    return render(request, 'user/create_event.html', {'title': 'Create event'})

# Returning password change page


def password_change(request):
    return render(request, 'user/change_password.html', {'title':'MUnite'})


def show_event(request, event_name):
    # id = Event.objects.only('id').get(event=event_name).id

    e = get_object_or_404(Event, event=event_name)
    D = [e.event, e.organization, e.date, e.venue, e.price, e.description]
    stuff_for_frontend = {
        'event': D
    }

    return render(request, 'user/event_description.html', stuff_for_frontend)
