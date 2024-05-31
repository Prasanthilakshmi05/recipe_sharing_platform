from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def _str_(self):
        return self.name

