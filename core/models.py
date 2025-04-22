from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=75)
    password = models.CharField(max_length=12)
    phone = models.PositiveIntegerField(null=True, blank=True)
    datebirth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'role')

class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    total_sessions = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(default=30)
    is_active = models.BooleanField(default=True)

class CoachService(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('coach', 'service')

class Product(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.PositiveIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name