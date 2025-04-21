from django.urls import path
from . import views
from core.views1.auth import SignUpView, LoginView, LogoutView, DeleteAccountView
from core.views1.pages import ServicesView, CartView, ProfileView, WelcomeLogView

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', CartView.as_view(), name='cart'),
    #path('cart/', views.cart, name='cart'),
    path('services/', ServicesView.as_view(), name='services'),
    #path('services/', views.services, name='services'),
    path('coaches/', views.coaches, name='coaches'),


    path('login/', LoginView.as_view(), name='login'),
    #path('login/', views.login, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('signup/', views.signup, name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    #path('profile/', views.profile, name='profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('code-password/', views.code_password, name='code_password'),
    path('new-password/', views.new_password, name='new_password'),
    path('success-checkout/', views.success_checkout, name='success_checkout'),
    path('success-password/', views.success_password, name='success_password'),
    path('success/', views.success, name='success'),
    path('welcome-log/', WelcomeLogView.as_view(), name='welcome_log'),
    #path('welcome-log/', views.welcome_log, name='welcome_log'),
    path('welcome-role/', views.welcome_role, name='welcome_role'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ##path('logout/', views.logout, name='logout'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete_account'),


    path('coaches/s1mple/', views.s1mple, name='s1mple'),
    path('coaches/sinatraa/', views.sinatraa, name='sinatraa'),
    path('coaches/tarik/', views.tarik, name='tarik'),
    path('coaches/tenz/', views.tenz, name='tenz'),
    path('coaches/xqc/', views.xqc, name='xqc'),
    path('coaches/zellsis/', views.zellsis, name='zellsis'),
]
