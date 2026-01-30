from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=150, default="undedfined")
    email = models.EmailField(unique=True, null=False)
    age = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=128, null=False)


def __str__(self):
        return self.username