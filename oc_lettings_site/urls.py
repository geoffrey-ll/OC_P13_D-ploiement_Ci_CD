from django.contrib import admin
from django.urls import include, path

from index.views import index


urlpatterns = [
    path('', index, name='index'),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path('admin/', admin.site.urls),
]
