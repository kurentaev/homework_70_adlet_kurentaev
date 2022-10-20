from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Login")
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)
