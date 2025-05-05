from django.urls import path
from core import views
from core.views import (
    LoginView, SignUpView, LogoutView, ForgotPasswordView,
    ProductListView, ProductCreateView, ProductUpdateView, 
    ProductDeleteView, ChangePasswordView, UpdateProfileView
)

urlpatterns = [
# ---------------------- Index ----------------------
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('coaches/', views.coaches, name='coaches'),
    path('advice/', views.random_advice, name='advice'),
    path('cart/', views.cart, name='cart'), # Protegido
    path('delete-account/', views.delete_account_view, name='delete_account'),

# ---------------------- Account ----------------------
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('new-password/', ChangePasswordView.as_view(), name='new_password'),
    path('profile/', views.profile, name='profile'),
    path('update/', UpdateProfileView.as_view(), name='update_profile'),
    path('code-password/', views.code_password, name='code_password'),

    # Bienvenida segun rol (protegido)
    path('welcome-log/', views.welcome_log, name='welcome_log'),
    path('welcome-role/', views.welcome_role, name='welcome_role'),

    # Check carrito
    path('success-checkout/', views.success_checkout, name='success_checkout'),

# ---------------------- CRUD staff ----------------------
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    
# ---------------------- Coaches ----------------------
    path('coaches/s1mple/', views.s1mple, name='s1mple'),
    path('coaches/sinatraa/', views.sinatraa, name='sinatraa'),
    path('coaches/tarik/', views.tarik, name='tarik'),
    path('coaches/tenz/', views.tenz, name='tenz'),
    path('coaches/xqc/', views.xqc, name='xqc'),
    path('coaches/zellsis/', views.zellsis, name='zellsis'),
]
