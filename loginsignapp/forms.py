from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

from modelsapp.models import UserProfileInfo  
from crispy_forms.helper import FormHelper

  
class SignupForm(UserCreationForm):  
    first_name = forms.CharField(max_length=300, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=300, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=200, help_text='Required. Invalid email address.')  
    class Meta:  
        model = User  
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    helper = FormHelper()


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfileInfo
        exclude = ('profile_picture',)

    helper = FormHelper()


class UpdateProfilePic(forms.Form):
    image = forms.ImageField()