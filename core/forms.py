from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import User
import re

# SignUpForm
class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'datebirth', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'datebirth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
            raise ValidationError("Enter a valid email address.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.match(r'^\d{7,8}$', str(phone)):
            raise ValidationError("Phone number must be 7 or 8 digits.")
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,12}$')
        if not password_regex.match(password):
            raise ValidationError("Password must be 8-12 characters, include an uppercase letter, number, and special character.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')

        if password and confirm and password != confirm:
            self.add_error('confirm_password', "Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# LoginForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

# ProfileForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'datebirth', 'phone']
        widgets = {
            'datebirth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.match(r'^\d{7,8}$', str(phone)):
            raise forms.ValidationError("Phone number must be 7 or 8 digits.")
        return phone
    

# ChangePasswordForm
class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,12}$')
        if not password_regex.match(password):
            raise forms.ValidationError("Password must be 8-12 characters, include an uppercase letter, number, and special character.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password and confirm and password != confirm:
            self.add_error("confirm_password", "Passwords do not match.")

# ForgotPasswordForm
class ForgotPasswordForm(forms.Form):
    username = forms.CharField(label="Username or Email")
