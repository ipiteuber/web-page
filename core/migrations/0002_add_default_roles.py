from django.db import migrations

def create_default_roles(apps, schema_editor):
    Role = apps.get_model('core', 'Role')
    
    Role.objects.update_or_create(
        role_name='client',
        defaults={'description': 'Common user'}
    )
    Role.objects.update_or_create(
        role_name='staff',
        defaults={'description': 'Employee with special access'}
    )
    Role.objects.update_or_create(
        role_name='admin',
        defaults={'description': 'Administrator'}
    )

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),  # Cambia si tu migración base tiene otro nombre
    ]

    operations = [
        migrations.RunPython(create_default_roles),
    ]
