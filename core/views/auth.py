from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from core.forms import SignUpForm
from core.models import User

class SignUpView(FormView):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('success') #Redirige al registrarse con exito

    def form_valid(self, form):
        # Guarda el nuevo usuario
        user = form.save(commit=False)
        user.password = make_password(form.cleaned_data['password']) #Encripta contrasena
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'account/log_in.html'
    form_class = AuthenticationForm

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