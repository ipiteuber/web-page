import requests
from django.shortcuts import get_object_or_404, render, redirect
from core import models
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from external_services.steam import get_steam_game_players
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView
from core.forms import SignUpForm, LoginForm, ForgotPasswordForm, ChangePasswordForm, UpdateProfileForm, ProductForm
from core.models import CartItem, User, Product
from django.contrib import messages

# Create your views here.

# ---------------------- Index ----------------------
def index(request):
    cs2_players = get_steam_game_players(730)
    return render(request, 'index/index.html', {'cs2_players': cs2_players})

@login_required
def services(request):
    services = Product.objects.filter(is_active=True)
    return render(request, 'index/services.html', {'services': services})

def coaches(request):
    return render(request, 'index/coaches.html')

# ---------------------- Account ----------------------
# Inicio de sesion de usuario
class LoginView(FormView):
    template_name = 'account/log_in.html'
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('welcome_role')
            return redirect('welcome_log')
        return super().dispatch(request, *args, **kwargs)
    
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

# Registro de usuario
class SignUpView(FormView):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login') # Redirige al registrarse con exito

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Guarda el nuevo usuario
        user = form.save(commit=False) # Crea instancia con datos del form
        user.password = make_password(form.cleaned_data['password']) # Encripta contrasena
        user.save() # Guarda usuario en BD
        self.request.session['just_registered'] = True # Marca que usuario se registro
        return super().form_valid(form)

# Recuperacion contrasena
class ForgotPasswordView(FormView):
    template_name = 'account/forgot_password.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('new_password')

    def form_valid(self, form):
        username_or_email = form.cleaned_data.get('username')
        idnumber = self.request.POST.get('idnumber')
        datebirth = self.request.POST.get('datebirth')

        try:
            user = User.objects.get(
                models.Q(username=username_or_email) | models.Q(email=username_or_email),
                idnumber=idnumber,
                datebirth=datebirth
            )
            self.request.session['reset_user_id'] = user.id
            return super().form_valid(form)
        except User.DoesNotExist:
            form.add_error(None, "No user matches those credentials.")
            return self.form_invalid(form)

# Logout
class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')

def success(request):
    if request.session.get('just_registered'):
        del request.session['just_registered']
        return render(request, 'account/log_in.html')
    return redirect('signup')

# Cambio de contrasena para recuperacion
class ChangePasswordView(FormView):
    template_name = 'account/new_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('login')  # Redirige a login

    def form_valid(self, form):
        user_id = self.request.session.get('reset_user_id')

        if not user_id:
            return redirect('forgot_password')

        try:
            user = User.objects.get(pk=user_id)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            del self.request.session['reset_user_id']  # Limpia la sesion
            return super().form_valid(form)
        except User.DoesNotExist:
            return redirect('forgot_password')


# ---------------------- Account @login_required ----------------------
@login_required
def profile(request):
    return render(request, 'account/profile.html', {'user': request.user})

# Actualizacion de perfil
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'account/update_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        if password:
            form.instance.password = make_password(password)
        return super().form_valid(form)

@login_required
def code_password(request):
    return render(request, 'account/code_password.html')

@login_required
def new_password(request):
    if not request.session.get('reset_user_id'):
        return redirect('forgot_password')
    return render(request, 'account/new_password.html')

@login_required
def welcome_log(request):
    return render(request, 'account/welcome_log.html')

@login_required
def welcome_role(request):
    return render(request, 'account/welcome_role.html')

@login_required
def delete_account_view(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Cierra sesion antes de eliminar
        user.delete()
        return redirect('index')
    
# ---------------------- Products (CRUD staff) ----------------------
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ProductListView(StaffRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductCreateView(StaffRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(StaffRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(StaffRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


# ---------------------- Coaches ----------------------
def s1mple(request):
    return render(request, 'coaches/s1mple.html')

def sinatraa(request):
    return render(request, 'coaches/sinatraa.html')

def tarik(request):
    return render(request, 'coaches/tarik.html')

def tenz(request):
    return render(request, 'coaches/tenz.html')

def xqc(request):
    return render(request, 'coaches/xqc.html')

def zellsis(request):
    return render(request, 'coaches/zellsis.html')


# ---------------------- Cart ----------------------
@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user).select_related('product')
    total = sum(i.product.price * i.quantity for i in items)
    return render(request, 'index/cart.html', {
        'cart_items': items,
        'total': total
    })

@login_required
def cart_add(request, product_id):
    if request.method == 'POST':
        p = get_object_or_404(Product, pk=product_id)
        item, created = CartItem.objects.get_or_create(user=request.user, product=p)
        if not created:
            item.quantity = F('quantity') + 1
        item.save()
    return redirect('cart')

@login_required
def cart_remove(request, item_id):
    if request.method == 'POST':
        ci = get_object_or_404(CartItem, pk=item_id, user=request.user)
        ci.delete()
    return redirect('cart')

@login_required
def success_checkout(request):
    if request.method == 'POST':
        CartItem.objects.filter(user=request.user).delete()
        return render(request, 'account/success_checkout.html')
    return redirect('cart')