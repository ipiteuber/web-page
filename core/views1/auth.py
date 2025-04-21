from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from core.forms import SignUpForm, LoginForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from core.models import User

# Gestion de autentificacion y gestion de cuenta

# Registro de usuario
class SignUpView(FormView):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('success') #Redirige al registrarse con exito

    def form_valid(self, form):
        # Guarda el nuevo usuario
        user = form.save(commit=False) # Crea instancia con datos del form
        user.password = make_password(form.cleaned_data['password']) # Encripta contrasena
        user.save() # Guarda usuario en BD
        return super().form_valid(form)

# Inicio de sesion de usuario
class LoginView(FormView):
    template_name = 'account/log_in.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(self.request, user)
            if user.is_staff:
                return redirect('welcome_role')
            else:
                return redirect('welcome_log')
        return self.form_invalid(form)

# Logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

# Elimina cuenta
class DeleteAccountView(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        user.delete()
        return redirect('deleted')
