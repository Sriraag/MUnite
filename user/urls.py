from django.urls import path, include 
from django.conf import settings 
from . import views 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth

from user import views
  
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('login/user/<str:username>', views.loggedin, name='user'),
    #url(r'^login/user/(?P<person_id>[0-9]+)$',
    #    'views.loggedin', name='user'),
    path('change_password', views.password_change, name='change_password'),
    path('login/', views.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('register/', views.register, name='register'),
] 
