from django.urls import path, include 
from django.conf import settings 
from . import views 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth

from user import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'), 
    path('event/<str:event_name>', views.show_event, name='event'),
    path('submitted', views.save_event, name='save_event'),
    path('user/<str:username>', views.loggedin, name='user'),
    path('create-event/<str:username>', views.create_event,  name='create_event'),
    path('change_password', views.password_change, name='change_password'),
    path('login/', views.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('register/', views.register, name='register'),
] 
