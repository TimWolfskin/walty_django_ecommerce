from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}))


    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    bio = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Bio"}))
    phone = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    class Meta:
        model = Profile
        fields = ['full_name', 'image', 'bio', 'phone']