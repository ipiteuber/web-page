from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import date

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=75)
    idnumber = models.CharField(max_length=9, unique=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    datebirth = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'fullname', 'idnumber', 'datebirth']

    def __str__(self):
        return self.username


class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'role'], name='unique_user_role')
        ]

    def __str__(self):
        return f"{self.user.username} -> {self.role.role_name}"


class Coach(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname       = models.CharField(max_length=50, unique=True)
    fullname       = models.CharField(max_length=100, null=True, blank=True)
    bio            = models.CharField(max_length=300, null=True, blank=True)
    total_sessions = models.PositiveIntegerField(default=0)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname

class Product(models.Model):
    name         = models.CharField(max_length=100)
    description  = models.TextField(blank=True)
    category     = models.CharField(max_length=50, blank=True)
    duration     = models.PositiveIntegerField(null=True, blank=True, help_text="Minutos (si aplica)")
    is_active    = models.BooleanField(default=True)
    image_path   = models.CharField(
                        max_length=200,
                        default='images/default.jpg',
                        help_text="Ruta dentro de static/images/"
                    )
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    stock        = models.PositiveIntegerField(default=0)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')