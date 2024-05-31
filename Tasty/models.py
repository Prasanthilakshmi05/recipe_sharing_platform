from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
def _str_(self):
        return self.username
