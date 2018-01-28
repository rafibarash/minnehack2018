from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text=None)
    first_name = forms.CharField(max_length=30, required=False, help_text=None)
    last_name = forms.CharField(max_length=30, required=False, help_text=None)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )