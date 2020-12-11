from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Exam_project.accounts.models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
