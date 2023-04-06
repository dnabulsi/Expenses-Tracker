from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Expense

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # keeps configurations in one place
    class Meta:
        # when the form validates it creates a new user
        model = User
        # fields to be shown on form
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class ExampleForm(forms.Form):
    my_date_field = forms.DateField()