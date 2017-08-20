from django.contrib.auth.models import User

from django import forms

class UserForm(forms.ModelForm):
    ## widget=forms/Passworinput is for covering password with asterixes when typg password
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        ##Meta is basically information about your class
        model = User
        fields = ["username", "email", "password"]