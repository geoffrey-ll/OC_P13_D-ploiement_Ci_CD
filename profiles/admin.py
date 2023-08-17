"""Admin de l'app profiles."""
from django.contrib import admin

from .models import Profile


admin.site.register(Profile)
