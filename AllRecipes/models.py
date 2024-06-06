from django.db import models

class Recipe(models.Model):
    bio = models.CharField(max_length=100)
    # Other fields...

    def __str__(self):
        return f"{self.bio}"  # Adjust this line as necessary

