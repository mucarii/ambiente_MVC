from django.db import models


# Create your models here.
class Modelo(models.Model):
    name = models.CharField(max_length=100)

    def uppercase_name(self):
        return self.name.upper()
