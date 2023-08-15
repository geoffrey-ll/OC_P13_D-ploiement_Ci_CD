"""Modèles pour l'app profiles."""
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Modèle des profiles."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
