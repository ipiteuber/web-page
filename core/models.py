from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=100, unique=True) # Unico y obligatorio
    username = models.CharField(max_length=20, unique=True) # Unico y obligatorio
    fullname = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    idnumber = models.CharField(max_length=9, unique=True, default="00000000") # Unico y obligatorio
    phone = models.PositiveIntegerField(null=True, blank=True) # Opcional
    datebirth = models.DateField(null=False, default=date(2000, 1, 1)) # Obligatorio
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        unique_together = ('user', 'role')

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