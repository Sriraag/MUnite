from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm , SetPasswordForm
from collections import OrderedDict
from .models import *


class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() 
    phone_no = forms.CharField(max_length = 20) 
    first_name = forms.CharField(max_length = 20) 
    last_name = forms.CharField(max_length = 20) 

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_no', 'password1', 'password2']


'''
class UserForm2(forms.ModelForm):

    class Meta:
        model = Delegate
        fields = ('first_name', 'last_name')


class UserImageForm(forms.ModelForm):

    class Meta:
        model = Delegate
        fields = ('profile_pic',)
'''

'''
class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
'''