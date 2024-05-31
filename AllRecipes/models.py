from django.db import models
class User(models.Model):
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username

