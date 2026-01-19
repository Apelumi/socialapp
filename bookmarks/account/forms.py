from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = User.objects.exclude(
            id = self.instance.id
        ).filter(
            email=data
        )
        if qs.exists():
            return forms.ValidationError("Email already exists")
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class  UserRegistration(forms.ModelForm):
    password = forms.CharField(
        label= "password",
        widget= forms.PasswordInput
    )

    password2 = forms.CharField(
        label = "Repeat password again",
        widget = forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = ['username','first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd['password2']:
            raise forms.ValidationError("you entered two different passwords")
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            return forms.ValidationError("User with the email already exists")
        return data