from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(models.Model):
    user = models.ForeignKey(AbstractUser, related_name='user', on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField()
    followers = models.ManyToManyField(AbstractUser, related_name='followers', on_delete=models.CASCADE)