from django.shortcuts import render

# Create your views here.

# Index
def index(request):
    return render(request, 'index/index.html')

def cart(request):
    return render(request, 'index/cart.html')

def services(request):
    return render(request, 'index/services.html')

def coaches(request):
    return render(request, 'index/coaches.html')

# Account
def login(request):
    return render(request, 'account/log_in.html')

def signup(request):
    return render(request, 'account/sign_up.html')

def profile(request):
    return render(request, 'account/profile.html')

def forgot_password(request):
    return render(request, 'account/forgot_password.html')

def code_password(request):
    return render(request, 'account/code_password.html')

def new_password(request):
    return render(request, 'account/new_password.html')

def success_checkout(request):
    return render(request, 'account/success_checkout.html')

def success_password(request):
    return render(request, 'account/success_password.html')

def success(request):
    return render(request, 'account/success.html')

def welcome_log(request):
    return render(request, 'account/welcome_log.html')

def welcome_role(request):
    return render(request, 'account/welcome_role.html')

# Coaches
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
