from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    # ... additional fields and methods as required e.g we will need to handle get_username(), get_full_name()

class CustomUser1(AbstractUser):
    bio = models.TextField(blank=True)
    # ... additional fields as needed


'''
🔑 AbstractBaseUser
- Purpose:
- The most basic class for creating a custom user model.
- Provides only the authentication-related fields and methods:
- password
- last_login
- Methods like set_password(), check_password().
- What it does NOT provide:
- No username, email, or other profile fields.
- No permissions or groups.
- Use case:
- When you want full control over your user model (e.g., replacing username with email, adding custom fields).
- You must implement required fields and managers yourself (like USERNAME_FIELD, is_active, is_staff, etc.).

👤 AbstractUser
- Purpose:
- A subclass of AbstractBaseUser that already includes Django’s default fields and permissions system.
- What it provides:
- All fields from AbstractBaseUser.
- Plus: username, first_name, last_name, email, is_staff, is_superuser, groups, user_permissions.
- Use case:
- When you want to extend the default Django user model with extra fields but keep the built-in authentication and permissions system.
- Example: adding phone_number or profile_picture while still using Django’s admin and auth seamlessly.

'''    