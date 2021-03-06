from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'phone_number', 'client_type')


class EditUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number')
