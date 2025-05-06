from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import User, Role, UserRole, Product
import re

# Registro de usuario
class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'idnumber', 'datebirth', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'datebirth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^\w+$', username):
            raise ValidationError("Username must be alphanumeric and without spaces.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
            raise ValidationError("Enter a valid email address.")
        return email

    def clean_idnumber(self):
        idnumber = self.cleaned_data.get('idnumber')
        # Valida que el idnumber tenga entre 8 y 9 digitos
        if len(str(idnumber)) < 8 or len(str(idnumber)) > 9:
            raise ValidationError("ID number must have between 8 and 9 digits.")
        return idnumber

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.match(r'^\d{7,8}$', str(phone)):
            raise ValidationError("Phone number must be 7 or 8 digits.")
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[<>@$!%*?&]).{8,12}$')
        # Valida que tenga las 4 validaciones de seguridad
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

        try:
        # Asignar rol "client" por defecto
            client_role = Role.objects.get(role_name="client") # Obtiene rol
            user_role = UserRole(user=user, role=client_role) # Asigna rol
        except Role.DoesNotExist:
            # Puedes manejar esto como quieras, lanzar un error o ignorarlo
            raise ValidationError("The default role 'client' does not exist.")


        return user

# Inicio de sesion
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

# Perfil
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

# Actualizacion de perfil
class UpdateProfileForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'datebirth', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password or confirm:
            if password != confirm:
                raise forms.ValidationError("Passwords do not match.")
            password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[<>@$!%*?&]).{8,12}$')
            # Valida que tenga las 4 validaciones de seguridad
            if not password_regex.match(password):
                raise forms.ValidationError("Password must be 8-12 chars, include an uppercase, number, and symbol.")

        return cleaned_data

# Recuperacion de contrasena
class ForgotPasswordForm(forms.Form):
    username = forms.CharField(label="Username or Email")
    idnumber = forms.IntegerField(label="ID Number")
    datebirth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))

# Cambio de contrasena para recuperacion
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

# Producto
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'duration', 'is_active', 'image_path', 'price', 'stock']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image_path': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }