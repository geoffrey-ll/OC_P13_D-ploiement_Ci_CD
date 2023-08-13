from django.contrib import admin
from django.urls import include, path

from .views import index


def trigger_error(request):
    """Test d'erreur avec Sentry."""
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("", index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
    path("/sentry-debug/", trigger_error)
]
