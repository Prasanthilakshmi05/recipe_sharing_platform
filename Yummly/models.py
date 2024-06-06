from django.db import models
class Yummy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    def _str_(self):
        return self.name

