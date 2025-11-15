from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)

        assign_role_permission(profile)

@receiver(post_save, sender=UserProfile)
def assign_role_permission(sender, instance, **kwargs):
    '''Assign permissions based on role whenever a UserProfile is saved'''
    user = instance.user

    # Clear existing permissions
    user.user_permissions.clear()

    if instance.role == 'Admin':
        # Admins get all book permissions
        perms = ['can_add_book', 'can_change_book', 'can_delete_book']
    elif instance.role == 'Librarian':
        # Librarians can add and change books
        perms = ['can_add_book', 'can_change_book']
    elif instance.role == 'Member':
        # Members can only view books (no custom perms needed)
        perms = []
    else:
        perms = []

    for codename in perms:
        try:
            permission = Permission.objects.get(codename=codename, content_type__app_label='relationship_app')
            user.user_permissions.add(permission)
        except Permission.DoesNotExist:
            pass
