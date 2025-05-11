from django.db import migrations

def create_default_roles(apps, schema_editor):
    Role = apps.get_model('core', 'Role')
    
    client_role, created = Role.objects.update_or_create(
        role_name='client',
        defaults={'description': 'Common user'}
    )
    print(f"Client role created: {created}")

    staff_role, created = Role.objects.update_or_create(
        role_name='staff',
        defaults={'description': 'Employee with special access'}
    )
    print(f"Staff role created: {created}")

    admin_role, created = Role.objects.update_or_create(
        role_name='admin',
        defaults={'description': 'Administrator'}
    )
    print(f"Admin role created: {created}")


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_roles),
    ]