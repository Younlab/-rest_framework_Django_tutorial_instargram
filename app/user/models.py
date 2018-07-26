from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='pofile_image', blank=True)
    site = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-pk']